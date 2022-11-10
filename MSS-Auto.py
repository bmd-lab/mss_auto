from pymatgen.core import Structure
import numpy as np
from os.path import isfile, join
from os import listdir,remove,rename,mkdir,getcwd,rmdir
import re
from shutil import copy
import  sys
import  getopt
pattern_id = r'[m][p][-]\d+'
opts,args = getopt.getopt(sys.argv[1:],'hl:d:n:',["help","length=",'direction=','name='])

def make_supercell(path_unit_cell, path_super_cell,direction):
    """
    Function:
    Make supercell according to the length
    of unit cell along with z direction,and
    the length of final supercell is at least
    15 anstrom.

    Parameters:
    path_poscar_cart: string
    The path of unit cell structure
    super_cell_dir: string
    The path of supercell structure
    """
    dic_line={'x':2,'y':3,'z':4}
    dic_supercell={'x':[[1,1,1],[2,1,1],[3,1,1],[4,1,1],[5,1,1],[6,1,1]],
                   'y':[[1,1,1],[1,2,1],[1,3,1],[1,4,1],[1,5,1],[1,6,1]],
                   'z':[[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6]]}
    files = [f for f in listdir(path_unit_cell)
                         if isfile(join(path_unit_cell, f))]
    print(len(files))
    for i in range(len(files)):
        file_read = open(path_unit_cell + '\\' + files[i], 'r')
        lines = file_read.readlines()
        l = np.array([float(lines[dic_line[direction]].split()[0]),
                      float(lines[dic_line[direction]].split()[1]),
                      float(lines[dic_line[direction]].split()[2])])
        ll = l * l
        L = np.sqrt(ll[0] + ll[1] + ll[2])
        if L >= 15:
            id = re.search(pattern_id, files[i]).group()
            struc = Structure.from_file(path_unit_cell
                                        + '\\' + files[i])
            struc.make_supercell(dic_supercell[direction][0])
            struc.to(filename=path_super_cell + '\\' + id + str("POSCAR"))
            print(id, ' has make supercell ',dic_supercell[direction][0])
        elif 7.5 <= L < 15:
            id = re.search(pattern_id, files[i]).group()
            struc = Structure.from_file(path_unit_cell + '\\'
                                        + files[i])
            struc.make_supercell(dic_supercell[direction][1])
            struc.to(filename=path_super_cell + '\\' + id + str("POSCAR"))
            print(id, ' has make supercell ',dic_supercell[direction][1])
        elif 5 <= L < 7.5:
            id = re.search(pattern_id, files[i]).group()
            struc = Structure.from_file(path_unit_cell + '\\'
                                        + files[i])
            struc.make_supercell(dic_supercell[direction][2])
            struc.to(filename=path_super_cell + '\\' + id + str("POSCAR"))
            print(id, ' has make supercell ',dic_supercell[direction][2])
        elif 3.75 <= L < 5:
            id = re.search(pattern_id, files[i]).group()
            # print(id)
            struc = Structure.from_file(path_unit_cell + '\\'
                                        + files[i])
            struc.make_supercell(dic_supercell[direction][3])
            struc.to(filename=path_super_cell + '\\' + id + str("POSCAR"))
            print(id, ' has make supercell ',dic_supercell[direction][3])
        elif 3 <= L < 3.75:
            id = re.search(pattern_id, files[i]).group()
            struc = Structure.from_file(path_unit_cell + '\\'
                                        + files[i])
            struc.make_supercell(dic_supercell[direction][4])
            struc.to(filename=path_super_cell + '\\' + id + str("POSCAR"))
            print(id, ' has make supercell ',dic_supercell[direction][4])
        elif 2.5 <= L < 3:
            id = re.search(pattern_id, files[i]).group()
            struc = Structure.from_file(path_unit_cell + '\\'
                                        + files[i])
            struc.make_supercell(dic_supercell[direction][5])
            struc.to(filename=path_super_cell + '\\' + id + str("POSCAR"))
            print(id, ' has make supercell ',dic_supercell[direction][5])

def add_atom(path_1, path_2,direction):
    """
    Function:
    Produce 1600 different supercell files that the fake
    atom in different position of box for every supercell

    Parameters:
    path_1: string
    The path of POSCAR(super cell),and it must be direction coordinate
    path_2: string
    The path of POSCAR files that contain a fake atom,
    and it will include 1600 different cases.

    """
    for i in range(100):  # i is the z coordinate of fake atom
        with open(path_1, 'r') as f:
            lines = f.readlines()
            lines[6] = (lines[6].strip('\n')) + ' 1' + '\n'  # add one for  atom number
            lines[5] = (lines[5].strip('\n')) + ' X' + '\n'  # suppose the fake atom is X
        for m in np.arange(0.05, 0.95, 0.25):  # m is the x coordinate of fake atom
            for n in np.arange(0.05, 0.95, 0.25):  # m is the y coordinate of fake atom
                with open(path_2 + '//' + 'POSCAR'
                          + '_' + str(m) + '_'
                          + str(n) + '_' + str(i), 'w+') as l:
                    for j in range(len(lines)):
                        l.write(lines[j])
                    if direction == 'x':
                        l.write(str(i * 0.01 + 0.005) + ' ' +
                                str(m) + ' ' +
                                str(n) + ' X')
                    elif direction == 'y':
                        l.write(str(m) + ' ' +
                                str(i * 0.01 + 0.005) + ' ' +
                                str(n) + ' X')
                    elif direction == 'z':
                        l.write(str(m) + ' ' +
                                str(n) + ' ' +
                                str(i * 0.01 + 0.005) + ' X')

def delet_file(Dir, File):
    # delet files in Dir except File
    files = [f for f in listdir(Dir) if isfile(join(Dir, f))]
    for i in files:
        if i == File:
            pass
        else:
            remove(Dir + '//' + i)

def get_nearest_distance(path):
    """
    Return the list of minimum distance to fake atom of all supercells
    and the corresponding structures.

    Parameters
    path:  string
    The path to the folder containing supercells files,and the supercell
    must be already added with fake atom.
    """
    files = [f for f in listdir(path) if isfile(join(path, f))]
    distance, structure = [], []
    for i in range(len(files)):
        s = Structure.from_file(path + '//' + files[i])
        d = s.distance_matrix
        t = d[:, -1]
        tt = np.delete(t, [-1])
        min_d = np.min(tt)
        distance.append(min_d)
        structure.append(files[i])
    return distance, structure

def dir_trans_cart(dir_path, cart_path):
    """
    Function:
    Transform the coordinate of POSCAR from direction
    to cartesian in batch.

    Parameters
    dir_path: string
    The path of POSCAR files with direction coordinate
    cart_path: string
    The path of POSCAR files that after convert into
    cartesian coordinate
    """
    onlyfiles = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
    for i in range(len(onlyfiles)):
        try:
            file_read = open(dir_path + "\\" + onlyfiles[i], 'r')
            line = file_read.readlines()
            file_read.close()
            a1 = float(line[2].split()[0])
            a2 = float(line[3].split()[0])
            a3 = float(line[4].split()[0])
            b1 = float(line[2].split()[1])
            b2 = float(line[3].split()[1])
            b3 = float(line[4].split()[1])
            c1 = float(line[2].split()[2])
            c2 = float(line[3].split()[2])
            c3 = float(line[4].split()[2])
            num_atoms = sum([int(x) for x in line[6].split()])
            x_cartesian = []
            y_cartesian = []
            z_cartesian = []
            start_num = 8
            for k in range(start_num, num_atoms + start_num):
                x_cartesian.append(
                    float(line[k].split()[0]) * a1
                    + float(line[k].split()[1])* a2
                    + float(line[k].split()[2]) * a3)
                y_cartesian.append(
                    float(line[k].split()[0]) * b1
                    + float(line[k].split()[1]) * b2
                    + float(line[k].split()[2]) * b3)
                z_cartesian.append(
                    float(line[k].split()[0]) * c1
                    + float(line[k].split()[1]) * c2
                    + float(line[k].split()[2]) * c3)
            with open(cart_path + "\\" + onlyfiles[i], "w", encoding="utf-8") as f:
                for j in range(7):
                    f.write(line[j])
                f.write("Cartesian\n")
                for l in range(num_atoms):
                    string = str(x_cartesian[l]) \
                             + "  " + str(y_cartesian[l]) \
                             + "  " + str(z_cartesian[l]) + "\n"
                    f.write(string)
        except:
            print(onlyfiles[i])

def Get_num_of_atom(path, file):
    # get the number of atoms in POSCAR
    # return a data of int type
    with open(path + '//' + file, 'r') as f:
        line = f.readlines()
        num_atoms = sum([int(x) for x in line[6].split()])
    return num_atoms

def insert_empty(dir1, dir2, distance, file,direction):
    """
    Function:
    Introduce an empty layer in the end of POSCAR
    along with z direction

   Parameters:
   dir1: string
   The path of origin POSCAR files and the coordinate of POSCAR
   can be direction or cartesian
   dir_2: string
   The path of POSCAR files that have introduced empty layer
   space
   distance: int
   The length of empty layer
   file: string
   Name of structure,such as :POSCAR,id+POSCAR
   """
    dic_line = {'x': 2, 'y': 3, 'z': 4}
    with open(dir1 + '//' + file, 'r') as f:
        lines = f.readlines()
        # print(len(lines))
        a, b, c = float(lines[dic_line[direction]].split()[0]), \
                  float(lines[dic_line[direction]].split()[1]), \
                  float(lines[dic_line[direction]].split()[2])
        # print(a,b,c)
        vector = np.array([a, b, c])
        length = np.sum(np.square(vector)) ** 0.5
        L = length + distance
        ratio = L / length
        new_vector = vector * ratio
        with open(dir2 + '//' + file, 'w') as f:
            lines[dic_line[direction]] = str(new_vector[0]) \
                       + ' ' + str(new_vector[1])\
                       + ' ' + str(new_vector[2]) + '\n'
            for i in lines:
                f.write(i)

def move_atom(dir1, atom_num, dir2, file, length,direction):
    """
    Function:
    Move atoms that higher than fake atom,
    equivalent to the effect of moving the
    vacuum layer.

    Parameters:
    dir1:  string
    The path of supercell files that
    contain vacuum layer,and the atoms haven't
    moved
    atom_num: int
    The number of atoms in POSCAR file
    dir2: string
    The path of supercell files that
    contain vacuum layer,and the atoms have
    moved according to the position of atoms
    file: string
    Name of structure,such as :POSCAR,id+POSCAR
    length: int
    The distance of atom need to be moved,
    it should stay the same with the
    length of vacuum layer
    """
    dic_num={'x':0, 'y':1,'z':2}
    with open(dir1 + '//' + file, 'r') as f:
        lines = f.readlines()
        high = float(lines[-1].split()[dic_num[direction]])
        #         print(z_fake)
        for i in range(atom_num - 1):
            x, y, z = float(lines[8 + i].split()[0]), \
                      float(lines[8 + i].split()[1]), \
                      float(lines[8 + i].split()[2])
            if direction == 'x':
                if high < 0 and x < high:
                    x_new = x - length
                    lines[8 + i] = str(x_new) + ' ' \
                                   + str(y) + ' ' \
                                   + str(z) + '\n'
                elif high > 0 and x > high:
                    x_new = x + length
                    lines[8 + i] = str(x_new) + ' ' \
                                   + str(y) + ' ' \
                                   + str(z) + '\n'
            elif direction == 'y':
                if high < 0 and y < high:
                    y_new = y - length
                    lines[8 + i] = str(x) + ' ' \
                                   + str(y_new) + ' ' \
                                   + str(z) + '\n'
                elif high > 0 and y > high:
                    y_new = y + length
                    lines[8 + i] = str(x) + ' ' \
                                   + str(y_new) + ' ' \
                                   + str(z) + '\n'
            elif direction == 'z':
                if high < 0 and z < high:
                    z_new = z - length
                    lines[8 + i] = str(x) + ' ' \
                                   + str(y) + ' ' \
                                   + str(z_new) + '\n'
                elif high > 0 and z > high:
                    z_new = z + length
                    lines[8 + i] = str(x) + ' ' \
                                   + str(y) + ' ' \
                                   + str(z_new) + '\n'
        with open(dir2 + '//' + file, 'w+') as f:
            for i in lines:
                f.write(i)

def delet_fake_atom(dir1, dir2, file):
    """
    Function:
    Delet the fake atom of slab structure

    Parameters:
    dir1: string
    The path of slab structure contained
    with fake atom
    dir2: string
    The path of slab structure that
    have deleted fake atom
    file: string
    Name of structure,such as :POSCAR,id+POSCAR
    """
    with open(dir1 + '//' + file, 'r') as f:
        lines = f.readlines()
        s = lines[5].split()
        s2 = lines[6].split()
        n_s, n_s2 = s[:-1], s2[:-1]
        line5, line6 = '', ''
        for i in range(len(n_s)):
            line5 += n_s[i] + ' '
            line6 += n_s2[i] + ' '
        new_line5 = line5 + '\n'
        new_line6 = line6 + '\n'
        #         print(new_line5,new_line6)
        lines[5], lines[6] = new_line5, new_line6
        with open(dir2 + '//' + file, 'w+') as f:
            for i in lines:
                f.write(i)

def main(length,direction,unit_cell_dir):
    name=unit_cell_dir.split('//')[-1]
    supercell_dir=unit_cell_dir[:-len(name)]+'super'
    slab_dir=unit_cell_dir[:-len(name)]+'slab'
    mkdir(supercell_dir)
    mkdir(slab_dir)

    make_supercell(unit_cell_dir, supercell_dir,direction)
    files=[f for f in listdir(supercell_dir) if isfile (join(supercell_dir,f))] 
    mkdir(slab_dir+'//Final_slab')
    for file in files:
        mkdir(slab_dir + '//' + file)
        mkdir(slab_dir + '//' + file + '/add')
        mkdir(slab_dir + '//' + file + '/cartesian')
        mkdir(slab_dir + '//' + file + '/add_empty')
        mkdir(slab_dir + '//' + file + '/move_atom')
        mkdir(slab_dir + '//' + file + '/final_slab')

        poscar_dir= slab_dir+'//'+file+"/add"
        cart_dir = slab_dir+'//'+file+"/cartesian"  
        insert_empty_dir = slab_dir+'//'+file+'/add_empty'  
        move_atom_dir = slab_dir+'//'+file+'/move_atom'  
        final_slab_dir = slab_dir+'//'+file+'/final_slab'

        s = Structure.from_file(supercell_dir + '//' + file)
        s.to(filename=slab_dir + '//' + file + '//' + 'POSCAR')  
        path_1 = slab_dir + '//' + file + '//' + 'POSCAR'  
        path_2 = slab_dir + '//' + file + '//' + 'add'  
        try:
            max_dis=[]
            add_atom(path_1, path_2, direction)
            d, stru = get_nearest_distance(path_2)
            max_dis.append(max(d))  
            delet_file(path_2, stru[d.index(max(d))])
            rename(path_2 + '//' + stru[d.index(max(d))], path_2 + '//' + file)
            print(file, 'is OK!!!')
        except:
            print(file, 'Happen something wrong')
        dir_trans_cart(poscar_dir,cart_dir)
        num = Get_num_of_atom(cart_dir, file)
        insert_empty(cart_dir,insert_empty_dir,length,file,direction)
        move_atom(insert_empty_dir, num, move_atom_dir, file,length,direction)
        delet_fake_atom(move_atom_dir, final_slab_dir, file)
        copy(final_slab_dir+'//'+file,slab_dir+'//Final_slab//'+file)
dir=getcwd()
unit_name,length,direction='','',''
try:
    for k, v in opts:
        if k in ('-n', '--name'):
            unit_name = v
        elif k in ('-l', '--length'):
            length = int(v)
        elif k in ('-d','--direction'):
            direction = v
        elif k in ('-h','--help'):
            print('Hello!! ','\n',
                  'Before running this script' \
                  ' you are expect to creat a new folder','\n',
                  'for storing the unit cell files' \
                  ' and fill the following three options','\n',
                  'with right information','\n'
                  'Options:','\n',
                  '-n,  --name   the name of '\
                  'unit cell folder','\n',
                  '-l,  --length   the length of '\
                  'empty layer','\n',
                  '-d,  --direction   the direction of ' \
                  'makeing supercell','\n'
                  )
    unit_dir=dir+'\\'+ unit_name
    main(length,direction,unit_dir)
except:
    rmdir(dir+'\\'+'slab')
    rmdir(dir+'\\'+'super')