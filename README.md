# README

MSS-Auto is an open-source software for making slab structures (MSS) in batch from a given unit cell automatically. All files are designed to work with the Vienna Ab Initio Software Package (VASP) POSCAR format. 
Before running the code, please be aware of the following:

## Requirements
 - pymatgen
 - numpy

## How to run it

With the MSS-Auto.py file in the working directory, first create a folder called "unit_cells".  Then place the unit cells you wish to transform inside the folder in the POSCAR format. The file name for each should be a unique string followed by "POSCAR" like this <id>+POSCAR. Then test MSS-Auto by typing 
 
     python MSS-Auto.py -h
     
you should get the following:

            Hello!
                 Before running this script, you are expecting to create a new folder named
                 unit_cell for storing the unit cell files and fill the following three options
                 with right information
                Options:
                 -n,  --name   the name of unit cell folder (if not unit_cells)
                 -l,  --length   the length of vacuum layer in Angstroms
                 -d,  --direction   the direction of making supercell, either 'x', 'y' or 'z'

So, you need to fill in at least the -n and -d options on your command line. For example,

        python MSS-Auto.py -l 10 -d z
        
this means you want to make slab supercell in the z direction and insert a 10 angstrom thick vacuum layer. You can also specify a different name for the folder containing the unit cells with the -n option.

## Output

If MSS-Auto.py ran successfully, the code will generate another two folders, 'super' and 'slab'.  The super folder contains supercell structure files, where the thickness is bigger than 15 angstroms along with the direction of your input. The slab folder may contain many subfolders, the slab structures we needed are in final slab folder, others are processing files that can help you check that the process ran successfully. 
 
 
 
 

        
        
        
