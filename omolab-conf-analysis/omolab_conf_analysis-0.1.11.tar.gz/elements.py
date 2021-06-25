import os
import pandas as pd
import numpy as np
import sys

class Element:
    def __init__(self,atomnum,min_bond_dist=1,max_bond_dist=2.5,min_num_bonds=1,max_num_bonds=8,coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates


class Carbon(Element):
    def __init__(self,atomnum,min_bond_dist=1.01,max_bond_dist=2.13,min_num_bonds=4,max_num_bonds=4, coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates


class Oxygen(Element):
    def __init__(self,atomnum,min_bond_dist=0.90,max_bond_dist=1.94,min_num_bonds=2,max_num_bonds=2, coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates


class Hydrogen(Element):
    def __init__(self,atomnum,min_bond_dist=0.70,max_bond_dist=1.64,min_num_bonds=1,max_num_bonds=1, coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates


class Nitrogen(Element):
    def __init__(self,atomnum,min_bond_dist=0.90,max_bond_dist=1.80,min_num_bonds=1,max_num_bonds=4, coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates


class Fluorine(Element):
    def __init__(self,atomnum,min_bond_dist=0.90,max_bond_dist=1.54,min_num_bonds=1,max_num_bonds=4, coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates


class Calcium(Element):
    def __init__(self,atomnum,min_bond_dist=1.66,max_bond_dist=2.34,min_num_bonds=1,max_num_bonds=4, coordinates = []):
        self.atom_num = atomnum
        self.min_bd = min_bond_dist
        self.max_bd = max_bond_dist
        self.min_nb = min_num_bonds
        self.max_nb = max_num_bonds
        self.cartesian = coordinates

# c1 = Carbon()
# print(c1.max_bd)
#
# o1 = Oxygen()
# print(o1.max_bd)

########################################################################################################################
#  Testing How Elements would work

# calc_distance = True
# calc_dihedrals = True
# user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/xyz_file_test"
# user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test"
# user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/cycloheptadecane_file_test"
#
# directory_files = os.listdir(user_input_directory)
# xyz_files = []
# xyz_index_list = []
# master_xyz_contents_list = []
# distances_indexes_list = []
# dihedral_indexes_list = []
# master_dist_contents_list = []
# calculations_list = []
#
#
# for file in directory_files:
#     if file.endswith(".xyz"):
#         xyz_files.append(file)
#
# complete_path = user_input_directory + "/" + xyz_files[0]
# print(complete_path)
# specific_file_object = open(complete_path)
# n_atoms = specific_file_object.readline()
# structure_name = specific_file_object.readline()
# coordinates_structure = specific_file_object.readlines()
# carbon_list = []
# hydrogen_list = []
# oxygen_list = []
# listofatoms = []
#
# atom_number = 1
# for line in coordinates_structure:
#     split_line = line.split()
#     if split_line[0] == "C":
#         print("C atom found")
#         carbon_instance = Carbon(atomnum=atom_number)
#         carbon_instance.cartesian = [split_line[1],split_line[2],split_line[3]]
#         carbon_list.append(carbon_instance)
#         listofatoms.append(carbon_instance)
#         atom_number = atom_number + 1
#
#     elif split_line[0] == "H":
#         print("H atom found")
#         hydrogen_instance = Hydrogen(atomnum=atom_number)
#         hydrogen_instance.cartesian = [split_line[1],split_line[2],split_line[3]]
#         hydrogen_list.append(hydrogen_instance)
#         listofatoms.append(hydrogen_instance)
#         atom_number = atom_number + 1
#
#     elif split_line[0] == "O":
#         print("O atom found")
#         oxygen_instance = Hydrogen(atomnum=atom_number)
#         oxygen_instance.cartesian = [split_line[1],split_line[2],split_line[3]]
#         oxygen_list.append(oxygen_instance)
#         listofatoms.append(oxygen_instance)
#         atom_number = atom_number + 1
#
#     else:
#         print(split_line)
#         atom_number = atom_number + 1
#
#
# print("C LIST length")
# print(len(carbon_list))
# print("C****************C")
# print()
#
# print("H LIST length")
# print(len(hydrogen_list))
# print("H****************H")
# print()
#
# print("O LIST length")
# print(len(oxygen_list))
# print("O****************O")
# print()

# for hydrogens in hydrogen_list:
#     print(hydrogens.cartesian)


def dist(atom1,atom2):
    a1 = atom1.cartesian
    a1_array = np.array(list(map(float,a1)))
    a2 = atom2.cartesian
    a2_array = np.array(list(map(float,a2)))
    v1 = a2_array - a1_array
    dist = np.linalg.norm(v1)
    return dist

#
# proper_dihedrals_atoms = []
# for atom1 in listofatoms:
#     for atom2 in listofatoms:
#         curr_distance = dist(atom1, atom2)
#         if atom1.atom_num != atom2.atom_num and atom1.min_bd < curr_distance < atom1.max_bd and atom2.min_bd < curr_distance <  atom2.max_bd:
#             # print(atom1.cartesian)
#             # print(atom2.cartesian)
#             # print(atom1.min_bd,atom1.max_bd)
#             # print(dist(atom1,atom2))
#             # print(atom2.min_bd,atom2.max_bd)
#             # sys.exit()
#
#             for atom3 in listofatoms:
#                 if atom3.atom_num > atom2.atom_num and atom3.atom_num != atom1.atom_num and atom2.min_bd < dist(atom2,atom3) < atom2.max_bd and atom3.min_bd < dist(atom2,atom3) <  atom3.max_bd:
#                     #we keep going
#                     for atom4 in listofatoms:
#                         if atom4.atom_num > atom1.atom_num and atom4.atom_num not in [atom1.atom_num,atom2.atom_num,atom3.atom_num] and atom3.min_bd < dist(atom3,atom4) < atom3.max_bd and atom4.min_bd < dist(atom3,atom4) < atom4.max_bd:
#                             print("True LOOP LAST")
#                             print("Atom1: ", atom1.atom_num)
#                             print("Atom2: ", atom2.atom_num)
#                             print("Atom3: ", atom3.atom_num)
#                             print("Atom4: ", atom4.atom_num)
#                             proper_dihedrals_atoms.append([atom1,atom2,atom3,atom4])
#
# # for items in proper_dihedrals_atoms:
# #     print(items[0].cartesian)
# #     print(items[1].cartesian)
# #     print(items[2].cartesian)
# #     print(items[3].cartesian)
# #     print()
# #     print()
# #     sys.exit()
#
# print(len(listofatoms))
# print(len(proper_dihedrals_atoms))
#
# for elements in proper_dihedrals_atoms:
#     for atoms in elements:
#         print(atoms.atom_num)
#
#     print()


# specific_file_object = open(complete_path)
# n_atoms_distangdih = specific_file_object.readline()
# n_atoms_distangdih = int(n_atoms_distangdih)
#
# atoms_list = list(range(1, n_atoms_distangdih + 1))
#
# print("Which atoms you would like to compute calculations on.")
# print("All you need to type is the atom NUMBER, no spaces (ex. 1,5,7,8,10)")
# print("If you would like all, enter 'all'")
#
# # userAtomsChoice = input("Atoms: ")
# atomsChoice = list(range(1, n_atoms_distangdih + 1)) #doing "all" for the first couple runs
#
# # if userAtomsChoice == "all":
# #     atomsChoice = list(range(1, n_atoms_distangdih + 1))
#
# # else:
# #     #  remove duplicates using set()
# #     split_Choices = userAtomsChoice.split(",")
# #
# #     # removing any possible empty strings
# #     # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
# #     split_Choices = list(filter(None, split_Choices))
# #
# #     atomsChoice = list(map(int, set(split_Choices)))
# #     atomsChoice.sort()
# #     #  list(map(int, test_list) will make each number in list an int
#
# atoms_list = atomsChoice
#
# print("Compute distances? Yes")
# for atom_1 in atoms_list:
#
#     for atom_2 in atoms_list:
#         if atom_2 > atom_1:
#             distances_indexes_list.append([atom_1, atom_2])
#
#
# # print("Would you like to compute angles? Y/N")
# # user_comp_angles = input("Angles (Y/N): ").upper()
# #
# # if user_comp_angles == "Y":
# #     print("Angles will be computed")
# #     comp_angles = True
# #     print()
# #     angles_indexes_list = []
# #
# #     for atom_1 in atoms_list:
# #
# #         for atom_2 in atoms_list:
# #             if atom_2 != atom_1:
# #
# #                 for atom_3 in atoms_list:
# #                     if atom_3 not in [atom_1, atom_2] and atom_3 > atom_1:
# #                         angles_indexes_list.append([atom_1, atom_2, atom_3])
# #
#
#
# print("Compute dihedrals? Yes")
# for atom_1 in atoms_list:
#
#     for atom_2 in atoms_list:
#         if atom_2 != atom_1:
#
#             for atom_3 in atoms_list:
#                 if atom_3 > atom_2 and atom_3 != atom_1:
#
#                     for atom_4 in atoms_list:
#
#                         if atom_4 not in [atom_1, atom_2, atom_3] and atom_4 > atom_1:
#                             dihedral_indexes_list.append([atom_1, atom_2, atom_3, atom_4])
#
#
# for file in xyz_files:
#     # print(file)  # test works to open xyz file
#     complete_path = user_input_directory + "/" + file  # need complete path to open file
#     specific_file_object = open(complete_path)
#
#     n_atoms = specific_file_object.readline()
#     n_atoms = int(n_atoms)
#     structure_name = specific_file_object.readline()  # subject to the operation performed prior to exporting XYZ; could change
#     temp_xyz_df = specific_file_object.readlines()
#     # print(temp_xyz_df)
#     temp_xyz_contents_list = []
#     temp_xyz_colname_list = []
#
#     xyz_index_list.append(file)  # should be file name, will be used to change index from number to file name
#     print("Files Found (updates):", xyz_index_list)
#     atom_num = 1
#
#     for elementxyzs in temp_xyz_df:
#         # print(elementxyzs)
#         split_elementxyzs = elementxyzs.split()
#         if (len(split_elementxyzs) > 0):  # necessary because at the end of each xyz file, there are three blank lines
#             # print(split_elementxyzs)
#             # print(split_elementxyzs[0]) atom name/element name
#             column_name = str(atom_num) + " " + split_elementxyzs[0]  # ex. 15 C; overall atom number and element
#
#             temp_xyz_contents_list.append(split_elementxyzs[1])
#             temp_xyz_colname_list.append(column_name + " -X")
#             temp_xyz_contents_list.append(split_elementxyzs[2])
#             temp_xyz_colname_list.append(column_name + " -Y")
#             temp_xyz_contents_list.append(split_elementxyzs[3])
#             temp_xyz_colname_list.append(column_name + " -Z")
#             atom_num += 1
#     master_xyz_contents_list.append(temp_xyz_contents_list)
#     print("Cartesian Cordinates: COMPLETE")
#
# test_xyz_df = pd.DataFrame(master_xyz_contents_list,
#                                columns=temp_xyz_colname_list)
# test_xyz_df.index = xyz_index_list
#
# # print(test_xyz_df)
#
# ## so we have the xyz's correctly done cool
#
# temp_dist_list = []
# dist_colname_list = []
#
# for dist_list in distances_indexes_list:
#     a1 = [float(temp_xyz_contents_list[3 * dist_list[0] - 3]),
#           float(temp_xyz_contents_list[3 * dist_list[0] - 2]),
#           float(temp_xyz_contents_list[3 * dist_list[0] - 1])]
#     a1_array = np.array(a1)
#
#     a2 = [float(temp_xyz_contents_list[3 * dist_list[1] - 3]),
#           float(temp_xyz_contents_list[3 * dist_list[1] - 2]),
#           float(temp_xyz_contents_list[3 * dist_list[1] - 1])]
#     a2_array = np.array(a2)
#
#     v1 = a2_array - a1_array
#     dist = np.linalg.norm(v1)
#     temp_dist_list.append(dist)
#     dist_colname_list.append(temp_xyz_colname_list[3 * dist_list[0] - 1][:-2] +
#                              "to " + temp_xyz_colname_list[3 * dist_list[1] - 1][:-2])  # Ex. 15 C to 18 H
#
# master_dist_contents_list.append(temp_dist_list)
# calculations_list.append(temp_dist_list)
# print("Distances: COMPLETE")
#
# test_dist_df = pd.DataFrame(master_dist_contents_list, columns=dist_colname_list)
# # test_dist_df.index = xyz_index_list
# print(test_dist_df)
# proper_dihedrals_indices = []
# #
# #I need to know which atom is which, this means when i read the file, I have to create an instance of the element
#
#
# # for indx,atom1 in enumerate(dihedral_indexes_list):
# #
# #     for indx2,atom2 in enumerate(dihedral_indexes_list):
# #         # if atom2 != atom1 and dist(atom1, atom2) > 0.8 and dist(atom1, atom2) < 1.7
# #         if atom2!= atom1 and calculations_list[indx+indx2] > 0.8
# # #             # we keep going
# # #
# # #             for atom3 in dihedral_indexes_list:
# #                 if atom2 not in [atom1, atom2] and dist(atom2, atom3) > 0.8
# #                     and dist(atom2, atom3) < 1.7:
# #                 # we keep going
# #
# #                 for atom4 in dihedral_indexes_list:
# #                     if atom4 not in [atom1, atom2, atom3] and dist(atom4, atom4) > 0.8
# #                         and dist(atom4, atom4) < 1.7:
# #
# #                 # this means if it gets this far, we have unique atoms that are
# #                 # "bonded" contiguously sorta
# #                 proper_dihedrals_indices.append([atom1, atom2, atom3, atom4])