# mss_auto
draft for  mss_auto software
# README
        MSS-Auto is an open-source software for making slab structure in batch from given unit cell. 
    Before running it, the following things you need to know.
# The dependent packages
### pymatgen
### numpy
# How to run it
             After create a folder for storing unit cell files, and put the MSS-Auto.py in the 
        same lever folder with that. Then you need prepare some unit cell files with POSCAR
        format and named id+POSCAR.You can open your terminal and switch to the catalog 
        containing MSS-Auto.py, inputting python MSS-Auto.py -h, you will get:
            Hello!!
                 Before running this script, you are expecting to create a new folder
                 for storing the unit cell files and fill the following three options
                 with right information
                Options:
                 -n,  --name   the name of unit cell folder
                 -l,  --length   the length of empty layer
                 -d,  --direction   the direction of making supercell
            So, you need to fill these messages in your command line, such as:
        python MSS-Auto.py -l 10 -d z -n unit, this means you want to make slab 
        from z direction, insert 10 angstrom thickness empty layer, and the name of 
        folder storing unit cell files is unit.
# Output
            You will get another two folders, super and slab, if you run MSS-Auto.py successfully. 
        The super folder contains supercell files, which the thickness is bigger than 15 angstroms 
        along with the direction you input. And the slab folder may contain many subfolders, the slab
        structures we needed are in final slab folder, others are processing files that can help you check.  
 
 
 
 

        
        
        
