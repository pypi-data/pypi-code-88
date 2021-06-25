import os
from shutil import copy
import subprocess



def generate_pymol(xyz_directory):
    print("If you do not want to generate a pymol session, enter 'exit'")
    filenames_to_pymol = input("File Names: ").split()
    if filenames_to_pymol[0].lower() == "exit":
        return

    print("File Names Received")
    print("Files to print below")
    for file in filenames_to_pymol:
        print(file)

    print(filenames_to_pymol)
    print()
    print("Please create a New Folder to copy structures into")
    current_directory = os.getcwd()
    added_xyz_folder_path = input("Enter New Folder Name: ")
    xyz_folder_path = os.path.join(current_directory,added_xyz_folder_path)

    os.mkdir(xyz_folder_path)
    print("Folder Created")
    # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test"
    user_input_directory = xyz_directory
    xyz_files_dir = os.listdir(user_input_directory)

    xyz_files = []
    for file in xyz_files_dir:
        if file.endswith(".xyz"):
            xyz_files.append(file)

    print("Printing all possible XYZ Files in question to be able to see in PyMol ")
    print(xyz_files)

    #  if there is a file in filenames_to_Pymol, that matches a file in xyz_files_dir, then
    for current_file in filenames_to_pymol:
        for current_file2 in xyz_files:
            if current_file == current_file2:
                #  copy file to the new directory path
                file_name = current_file2
                print("Copying " + file_name + " ...")
                print(xyz_folder_path)
                current_file_path = os.path.join(user_input_directory, file_name)
                copy(current_file_path, xyz_folder_path)

    os.chdir(xyz_folder_path)
    print("Directory Changed")
    # subprocess.Popen("mGenerate_PyMOL_Session.sh", cwd=None, shell= True)
    subprocess.Popen("mGenerate_PyMOL_Session.sh", cwd=None, shell= True)


# testing function
#/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test
# generate_pymol("/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test")



#take in post clustering pd.df that contains name of file and its corresponding family

def family_files(df_pc_clustering_final, num_clusters,files_directory):
    directory_files = os.listdir(files_directory) #this is the directory that they typed in at the beginning
    xyz_files = []
    
    #change directory to location of xyz files
    os.chdir(files_directory)

    #create folder-->
    family_holder_name = input("Enter folder name for families: ")
    current_file_path3 = os.path.join(os.getcwd(),family_holder_name)
    os.mkdir(current_file_path3)
    os.chdir(current_file_path3)

    family_directories = []
    
    for nums in range(1,num_clusters+1):
        #create folder
        new_directory = "Family " + str(nums)
        path = os.path.join(current_file_path3,new_directory)
        os.mkdir(path)
        family_directories.append(path) #save for later ;)
        
    # at this point, all folders have been created
    
    for index, row in df_pc_clustering_final.iterrows():
        family = row["Families"]
        current_file = os.path.join(files_directory,index)
        new_file_location = os.path.join(current_file_path3,family)
        copy(current_file,new_file_location)
        
    print()
    print("Files have been put in their respective family folders")
    
    
    
    # 
    # for file in directory_files:
    #     if file.endswith(".xyz"):
    #         #at this point, we are with a specific file. ex. tamylOH_7.xyz
    #         
    #         for row in df:
    #             if row.index (name) == file:
    #                 copy file to specific family directory
    #                 family = row["Families"]
    #                 path2 = os.path.join(directory_files,family)
    # 
    #                 from shutil import copyfile
    #                 copyfile(file (has to be full path), dst)
    #                 row["Families"]
                    






