# Create dataframe with xyz contents
import pandas as pd
import numpy as np
import elements
import sys
import math
master_xyz_contents_list = []
master_dist_contents_list = []
master_angle_contents_list = []
master_dihedral_contents_list = []
calculations_list = []


class InvalidUserEntranceError(Exception):
    def __init__(self, message):
        self.message = message


def calc_distances(distances_indexes_list,temp_xyz_contents_list,temp_xyz_colname_list):
    temp_dist_list = []
    dist_colname_list = []

    for dist_list in distances_indexes_list:
        a1 = [float(temp_xyz_contents_list[3 * dist_list[0] - 3]),
              float(temp_xyz_contents_list[3 * dist_list[0] - 2]),
              float(temp_xyz_contents_list[3 * dist_list[0] - 1])]
        a1_array = np.array(a1)

        a2 = [float(temp_xyz_contents_list[3 * dist_list[1] - 3]),
              float(temp_xyz_contents_list[3 * dist_list[1] - 2]),
              float(temp_xyz_contents_list[3 * dist_list[1] - 1])]
        a2_array = np.array(a2)

        v1 = a2_array - a1_array
        dist = np.linalg.norm(v1)
        temp_dist_list.append(dist)
        dist_colname_list.append(temp_xyz_colname_list[3 * dist_list[0] - 1][:-2] +
                                 "to " + temp_xyz_colname_list[3 * dist_list[1] - 1][:-2])  # Ex. 15 C to 18 H

    master_dist_contents_list.append(temp_dist_list)
    calculations_list.append(temp_dist_list)
    print("Distances: COMPLETE")
    return master_dist_contents_list,dist_colname_list


def calc_angles(angles_indexes_list,temp_xyz_contents_list,temp_xyz_colname_list):
    temp_angle_list = []
    angle_colname_list = []

    for angle_list in angles_indexes_list:
        a1 = [float(temp_xyz_contents_list[3 * angle_list[0] - 3]),
              float(temp_xyz_contents_list[3 * angle_list[0] - 2]),
              float(temp_xyz_contents_list[3 * angle_list[0] - 1])]
        a1_array = np.array(a1)

        a2 = [float(temp_xyz_contents_list[3 * angle_list[1] - 3]),
              float(temp_xyz_contents_list[3 * angle_list[1] - 2]),
              float(temp_xyz_contents_list[3 * angle_list[1] - 1])]
        a2_array = np.array(a2)

        a3 = [float(temp_xyz_contents_list[3 * angle_list[2] - 3]),
              float(temp_xyz_contents_list[3 * angle_list[2] - 2]),
              float(temp_xyz_contents_list[3 * angle_list[2] - 1])]
        a3_array = np.array(a3)

        v1 = a2_array - a1_array
        v2 = a3_array - a2_array
        da = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))  # in radians
        da_degrees = np.degrees(da)
        temp_angle_list.append(da_degrees)

        angle_colname_list.append(temp_xyz_colname_list[3 * angle_list[0] - 1][:-2] +
                                  "to " + temp_xyz_colname_list[3 * angle_list[1] - 1][:-2] +
                                  "to " + temp_xyz_colname_list[3 * angle_list[2] - 1][:-2])  # Ex. 15 C to 18 H

    master_angle_contents_list.append(temp_angle_list)
    print("Angles: COMPLETE")
    return master_angle_contents_list,angle_colname_list


def calc_dihedrals(dihedral_indexes_list,temp_xyz_contents_list,temp_xyz_colname_list):
    temp_dihedral_list = []
    dihedral_colname_list = []

    for di_list in dihedral_indexes_list:
        a1 = [float(temp_xyz_contents_list[3 * di_list[0] - 3]),
              float(temp_xyz_contents_list[3 * di_list[0] - 2]),
              float(temp_xyz_contents_list[3 * di_list[0] - 1])]
        a1_array = np.array(a1)

        a2 = [float(temp_xyz_contents_list[3 * di_list[1] - 3]),
              float(temp_xyz_contents_list[3 * di_list[1] - 2]),
              float(temp_xyz_contents_list[3 * di_list[1] - 1])]
        a2_array = np.array(a2)

        a3 = [float(temp_xyz_contents_list[3 * di_list[2] - 3]),
              float(temp_xyz_contents_list[3 * di_list[2] - 2]),
              float(temp_xyz_contents_list[3 * di_list[2] - 1])]
        a3_array = np.array(a3)

        a4 = [float(temp_xyz_contents_list[3 * di_list[3] - 3]),
              float(temp_xyz_contents_list[3 * di_list[3] - 2]),
              float(temp_xyz_contents_list[3 * di_list[3] - 1])]
        a4_array = np.array(a4)

        v1 = a2_array - a1_array
        v2 = a3_array - a2_array
        n1 = np.cross(v1, v2)  # cross product
        v3 = a2_array - a3_array
        v4 = a4_array - a3_array
        n2 = np.cross(v3, v4)

        dihedral = np.arccos(np.round(-np.dot(n1, n2) / (np.linalg.norm(n1) * np.linalg.norm(n2)), decimals=4))
        # radians ^

        if np.dot(n1, v4) > 0:
            dihedral = -1 * dihedral

        dihedral_degrees = np.degrees(dihedral)

        # MODIFICATION OF DIHEDRALS (NO LONGER ACTUAL DIHEDRALS)
        if 90 < dihedral_degrees < 180:
            dihedral_degrees = 180 - dihedral_degrees

        elif -90 > dihedral_degrees > -180:
            dihedral_degrees = -180 - dihedral_degrees

        temp_dihedral_list.append(dihedral_degrees)

        dihedral_colname_list.append(temp_xyz_colname_list[3 * di_list[0] - 1][:-2] +
                                     "to " + temp_xyz_colname_list[3 * di_list[1] - 1][:-2] +
                                     "to " + temp_xyz_colname_list[3 * di_list[2] - 1][:-2] +
                                     "to " + temp_xyz_colname_list[3 * di_list[3] - 1][:-2])
        # Ex. 1 C to 12 H to 20 F to 21 C
    master_dihedral_contents_list.append(temp_dihedral_list)
    print("Dihedrals: COMPLETE")
    print()
    print()

    return master_dihedral_contents_list,dihedral_colname_list

def calc_dihedrals_new(proper_dihedrals,temp_xyz_contents_list,temp_xyz_colname_list):
    temp_dihedral_list = []
    dihedral_colname_list = []

    for di_list in proper_dihedrals:
        a1 = [float(temp_xyz_contents_list[3 * di_list[0].atom_num - 3]),
              float(temp_xyz_contents_list[3 * di_list[0].atom_num - 2]),
              float(temp_xyz_contents_list[3 * di_list[0].atom_num - 1])]
        a1_array = np.array(a1)

        a2 = [float(temp_xyz_contents_list[3 * di_list[1].atom_num - 3]),
              float(temp_xyz_contents_list[3 * di_list[1].atom_num - 2]),
              float(temp_xyz_contents_list[3 * di_list[1].atom_num - 1])]
        a2_array = np.array(a2)

        a3 = [float(temp_xyz_contents_list[3 * di_list[2].atom_num - 3]),
              float(temp_xyz_contents_list[3 * di_list[2].atom_num - 2]),
              float(temp_xyz_contents_list[3 * di_list[2].atom_num - 1])]
        a3_array = np.array(a3)

        a4 = [float(temp_xyz_contents_list[3 * di_list[3].atom_num - 3]),
              float(temp_xyz_contents_list[3 * di_list[3].atom_num - 2]),
              float(temp_xyz_contents_list[3 * di_list[3].atom_num - 1])]
        a4_array = np.array(a4)

        v1 = a2_array - a1_array
        v2 = a3_array - a2_array
        n1 = np.cross(v1, v2)  # cross product
        v3 = a2_array - a3_array
        v4 = a4_array - a3_array
        n2 = np.cross(v3, v4)

        dihedral = np.arccos(np.round(-np.dot(n1, n2) / (np.linalg.norm(n1) * np.linalg.norm(n2)), decimals=4))
        # radians ^

        if np.dot(n1, v4) > 0:
            dihedral = -1 * dihedral

        dihedral_degrees = np.degrees(dihedral)

        # MODIFICATION OF DIHEDRALS (NO LONGER ACTUAL DIHEDRALS)
        if 90 < dihedral_degrees < 180:
            dihedral_degrees = 180 - dihedral_degrees

        elif -90 > dihedral_degrees > -180:
            dihedral_degrees = -180 - dihedral_degrees

        temp_dihedral_list.append(dihedral_degrees)

        dihedral_colname_list.append(temp_xyz_colname_list[3 * di_list[0].atom_num - 1][:-2] +
                                     "to " + temp_xyz_colname_list[3 * di_list[1].atom_num - 1][:-2] +
                                     "to " + temp_xyz_colname_list[3 * di_list[2].atom_num - 1][:-2] +
                                     "to " + temp_xyz_colname_list[3 * di_list[3].atom_num - 1][:-2])
        # Ex. 1 C to 12 H to 20 F to 21 C
    master_dihedral_contents_list.append(temp_dihedral_list)
    print("Dihedrals: COMPLETE")
    print()
    print()

    return master_dihedral_contents_list,dihedral_colname_list

#  Goal 1: Grab XYZ Content

def xyz_contents(xyz_files, user_directory):
    xyz_index_list = []
    comp_distances = False
    comp_angles = False
    comp_dihedrals = False
    atoms_list = None

    while True:
        try:
            complete_path = user_directory + "/" + xyz_files[0]
            specific_file_object = open(complete_path)
            n_atoms_distangdih = specific_file_object.readline()
            n_atoms_distangdih = int(n_atoms_distangdih)
            structure_name = specific_file_object.readline()
            coordinates_structure = specific_file_object.readlines()
            carbon_list = []
            hydrogen_list = []
            oxygen_list = []
            nitrogen_list = []
            fluorine_list = []
            listofatoms = []

            atoms_list = list(range(1, n_atoms_distangdih + 1))

            print("Which atoms you would like to compute calculations on.")
            print("All you need to type is the atom NUMBER, no spaces (ex. 1,5,7,8,10)")
            print("Enter in elements to choose specfic elements (ex. O,C,H)")
            print("If you would like all, enter 'all'")

            userAtomsChoice = input("Atoms/Elements: ")

            #[s for s in mylist if s.isdigit()]
            # digits_Choices = [s for s in split_Choices if s.isdigit()]

            split_choices_atom_num = userAtomsChoice.replace(',', '')
            split_choices_atom_num = str(split_choices_atom_num)

            if userAtomsChoice.lower() == "all":  # option 1: all atoms will be used
                print("You chose to include all atoms")
                atomsChoice = list(range(1, n_atoms_distangdih + 1))

            elif split_choices_atom_num.isdigit(): # option 2: atoms selected by atom number will be used
                #  remove duplicates using set()
                print("You chose to include atoms via atom number")
                split_Choices = userAtomsChoice.split(",")

                # removing any possible empty strings
                # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
                split_Choices = list(filter(None, split_Choices))

                atomsChoice = list(map(int, set(split_Choices)))
                atomsChoice.sort()
                #  list(map(int, test_list) will make each number in list an int


            else: # option 3: atoms types (elements) only will be used
                print("You chose to include atoms via element")
                userAtomsChoice = userAtomsChoice.upper() # ensure that inputs are uppercase (O,N)
                # note: Ca will be CA --> this is taken note of later on
                atom_number = 1
                atomsChoice = []

                for line in coordinates_structure:
                    print(line)
                    split_line = line.split()
                    userAtoms_splitChoices = userAtomsChoice.split(",")

                    if split_line[0].upper() in userAtoms_splitChoices:
                        #upper here necessary bc all userAtomsChoices will be upper
                        #need to check if in conditional is case sensitive ----> YES they are
                        print("True")
                        print(split_line[0])
                        atomsChoice.append(atom_number)
                        print(atomsChoice)
                        atom_number = atom_number + 1

                    else:
                        atom_number = atom_number + 1

            '''
                  if userAtomsChioce is a list of elements (C,H,N) (option 2: using elements only)
                      do same reading as below for one molecule;

                      eg.
                      atom_number = 1
                      If split_line[0] is in userAtomsChoice list of elements
                          great, its one of the atoms we want

                          now do the same
                              if split_line[0] == "C":
                              # print("C atom found")
                              carbon_instance = elements.Carbon(atomnum=atom_number)
                              carbon_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                              carbon_list.append(carbon_instance)
                              listofatoms.append(carbon_instance)
                              atom_number = atom_number + 1

                  if it doesnt trigger the above if statement
                      atom_number = atom_number + 1


                  '''
            atoms_list = atomsChoice
            # print(atoms_list)
            atom_number = 1
            for line in coordinates_structure:
                print(line)
                if atom_number not in atoms_list:
                    # print("True")
                    # print(atom_number)
                    atom_number = atom_number + 1
                    continue
                else:
                    split_line = line.split()
                    if split_line[0] == "C":
                        # print("C atom found")
                        carbon_instance = elements.Carbon(atomnum=atom_number)
                        carbon_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                        carbon_list.append(carbon_instance)
                        listofatoms.append(carbon_instance)
                        atom_number = atom_number + 1

                    elif split_line[0] == "H":
                        # print("H atom found")
                        hydrogen_instance = elements.Hydrogen(atomnum=atom_number)
                        hydrogen_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                        hydrogen_list.append(hydrogen_instance)
                        listofatoms.append(hydrogen_instance)
                        atom_number = atom_number + 1

                    elif split_line[0] == "O":
                        # print("O atom found")
                        oxygen_instance = elements.Oxygen(atomnum=atom_number)
                        oxygen_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                        oxygen_list.append(oxygen_instance)
                        listofatoms.append(oxygen_instance)
                        atom_number = atom_number + 1

                    elif split_line[0] == "N":
                        # print("N atom found")
                        nitrogen_instance = elements.Nitrogen(atomnum=atom_number)
                        nitrogen_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                        nitrogen_list.append(nitrogen_instance)
                        listofatoms.append(nitrogen_instance)
                        atom_number = atom_number + 1

                    elif split_line[0] == "F":
                        # print("N atom found")
                        fluorine_instance = elements.Fluorine(atomnum=atom_number)
                        fluorine_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                        fluorine_list.append(fluorine_instance)
                        listofatoms.append(fluorine_instance)
                        atom_number = atom_number + 1

                    elif split_line[0] == "CA":
                        # print("N atom found")
                        calcium_instance = elements.Calcium(atomnum=atom_number)
                        calcium_instance.cartesian = [split_line[1], split_line[2], split_line[3]]
                        calcium_instance.append(calcium_instance)
                        listofatoms.append(calcium_instance)
                        atom_number = atom_number + 1

            print()
            print("Would you like to compute distances? Y/N")
            user_comp_distances = input("Distances (Y/N): ").upper()
            if user_comp_distances == "Y":
                print("Distances will be computed")
                comp_distances = True
                print()
                distances_indexes_list = []

                for atom_1 in atoms_list:

                    for atom_2 in atoms_list:
                        if atom_2 > atom_1:
                            distances_indexes_list.append([atom_1, atom_2])

                if not distances_indexes_list:
                    # this means that your criteria for atoms/elements creates no proper dihedrals
                    raise InvalidUserEntranceError("Error: Your criteria for atoms/elements creates no distances")

            elif user_comp_distances == "N":
                print("Distances will NOT be computed")
                comp_distances = False
                print()

            else:
                raise InvalidUserEntranceError("Error: Must Choose Y or N")

            print("Would you like to compute angles? Y/N")
            user_comp_angles = input("Angles (Y/N): ").upper()

            if user_comp_angles == "Y":
                print("Angles will be computed")
                comp_angles = True
                print()
                angles_indexes_list = []

                for atom_1 in atoms_list:

                    for atom_2 in atoms_list:
                        if atom_2 != atom_1:

                            for atom_3 in atoms_list:
                                if atom_3 not in [atom_1, atom_2] and atom_3 > atom_1:
                                    angles_indexes_list.append([atom_1,atom_2,atom_3])

                if not angles_indexes_list:
                    # this means that your criteria for atoms/elements creates no proper dihedrals
                    raise InvalidUserEntranceError("Error: Your criteria for atoms/elements creates no angles")

            elif user_comp_angles == "N":
                print("Angles will NOT be computed")
                comp_angles = False
                print()

            else:
                raise InvalidUserEntranceError("Error: Must Choose Y or N")

            print("Would you like to compute dihedrals? Y/N")
            user_comp_dihedrals = input("Dihedrals (Y/N): ").upper()

            if user_comp_dihedrals == "Y":
                print("Dihedrals will be computed")
                print()
                comp_dihedrals = True
                # dihedral_indexes_list = []
                #
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
                proper_dihedrals_atoms = []
                for atom1 in listofatoms:
                    for atom2 in listofatoms:
                        curr_distance = elements.dist(atom1, atom2)
                        if atom1.atom_num != atom2.atom_num and atom1.min_bd < curr_distance < atom1.max_bd and atom2.min_bd < curr_distance < atom2.max_bd:
                            # print(atom1.cartesian)
                            # print(atom2.cartesian)
                            # print(atom1.min_bd,atom1.max_bd)
                            # print(dist(atom1,atom2))
                            # print(atom2.min_bd,atom2.max_bd)
                            # sys.exit()

                            for atom3 in listofatoms:
                                if atom3.atom_num > atom2.atom_num and atom3.atom_num != atom1.atom_num and atom2.min_bd < elements.dist(
                                        atom2, atom3) < atom2.max_bd and atom3.min_bd < elements.dist(atom2,
                                                                                             atom3) < atom3.max_bd:
                                    # we keep going
                                    for atom4 in listofatoms:
                                        if atom4.atom_num > atom1.atom_num and atom4.atom_num not in [atom1.atom_num,
                                                                                                      atom2.atom_num,
                                                                                                      atom3.atom_num] and atom3.min_bd < elements.dist(
                                                atom3, atom4) < atom3.max_bd and atom4.min_bd < elements.dist(atom3,
                                                                                                     atom4) < atom4.max_bd:
                                            # print("True LOOP LAST")
                                            # print("Atom1: ", atom1.atom_num)
                                            # print("Atom2: ", atom2.atom_num)
                                            # print("Atom3: ", atom3.atom_num)
                                            # print("Atom4: ", atom4.atom_num)
                                            proper_dihedrals_atoms.append([atom1, atom2, atom3, atom4])

                                            """
                                            if [atom 2, atom 3] is in dihedral_indexes_list (but only position 1 and 2)
                                                                        [____, atom 2, atom 3, ___]
                                            if not any(isinstance([atom_4, atom_2, atom_3, atom_1], dihedral_indexes_list):
                                                test_equality = True
                                                
                                            if [atom 2, atom 3] is in dihedral_indexes_list[][1:2] 
                                            #
                                            # for dihedrals in dihedral_indexes_list:
                                            #     if atom_2 == dihedrals[1] and atom_3 == dihedrals[2] and atom_1 == dihedrals[3] and atom_4 == dihedrals[0]:
                                            #         test_equality = True
                                            #
                                            # if not test_equality:
                                            #     dihedral_indexes_list.append([atom_1, atom_2, atom_3, atom_4])
                                            """
                if not proper_dihedrals_atoms:
                    print(proper_dihedrals_atoms)
                    # this means that your criteria for atoms/elements creates no proper dihedrals
                    raise InvalidUserEntranceError(
                        "Error: Your criteria for atoms/elements creates no proper dihedrals")



            elif user_comp_dihedrals == "N":
                print("Dihedrals will NOT be computed")
                comp_dihedrals = False
                print()

            else:
                raise InvalidUserEntranceError("Error: Must Choose Y or N")

        except InvalidUserEntranceError as e:
            print()
            print(e.message)
            print("Restarting Questioning...")
            print()
            print("______________________________________________________")
            continue

        except ValueError:
            print()
            print("Value Error. You cannot put a word in list of atoms (integers)")
            print("Try Again...")
            print()
            print("______________________________________________________")
            continue
        break

    for file in xyz_files:
        # print(file)  # test works to open xyz file
        complete_path = user_directory + "/" + file  # need complete path to open file
        specific_file_object = open(complete_path)

        n_atoms = specific_file_object.readline()
        n_atoms = int(n_atoms)
        structure_name = specific_file_object.readline()  # subject to the operation performed prior to exporting XYZ; could change
        temp_xyz_df = specific_file_object.readlines()
        # print(temp_xyz_df)
        temp_xyz_contents_list = []
        temp_xyz_colname_list = []

        xyz_index_list.append(file)  # should be file name, will be used to change index from number to file name
        print("Files Found (updates):",xyz_index_list)
        atom_num = 1

        # XYZ
        #  Getting XYZ Content (Cartesian Coordinates)
        for elementxyzs in temp_xyz_df:
            # print(elementxyzs)
            split_elementxyzs = elementxyzs.split()
            if (len(split_elementxyzs) > 0):  # necessary because at the end of each xyz file, there are three blank lines
                # print(split_elementxyzs)
                # print(split_elementxyzs[0]) atom name/element name
                column_name = str(atom_num) + " " + split_elementxyzs[0]  # ex. 15 C; overall atom number and element

                temp_xyz_contents_list.append(split_elementxyzs[1])
                temp_xyz_colname_list.append(column_name + " -X")
                temp_xyz_contents_list.append(split_elementxyzs[2])
                temp_xyz_colname_list.append(column_name + " -Y")
                temp_xyz_contents_list.append(split_elementxyzs[3])
                temp_xyz_colname_list.append(column_name + " -Z")
                atom_num += 1
        master_xyz_contents_list.append(temp_xyz_contents_list)
        print("Cartesian Cordinates: COMPLETE")

        # DISTANCES
        # Getting Distances from each atom to all others
        if comp_distances:
            distances_calcs, distances_colmn = calc_distances(distances_indexes_list,temp_xyz_contents_list,
                                                                temp_xyz_colname_list)
        # ANGLES
        # Getting Angles from each atom to all others
        if comp_angles:
            angles_calcs, angles_colmn = calc_angles(angles_indexes_list,temp_xyz_contents_list,
                                                       temp_xyz_colname_list)
        # Dihedrals
        # Getting Dihedrals from each atom to all others
        if comp_dihedrals:
            # dihedral_calcs, dihedrals_colmn = calc_dihedrals(dihedral_indexes_list,temp_xyz_contents_list,
            #                                                    temp_xyz_colname_list)

            dihedral_calcs, dihedrals_colmn = calc_dihedrals_new(proper_dihedrals_atoms, temp_xyz_contents_list,
                                                             temp_xyz_colname_list)

    test_xyz_df = pd.DataFrame(master_xyz_contents_list,
                               columns=temp_xyz_colname_list)
    test_xyz_df.index = xyz_index_list

    if comp_distances:
        test_dist_df = pd.DataFrame(distances_calcs,
                                    columns=distances_colmn)
        test_dist_df.index = xyz_index_list

    if comp_angles:
        test_angle_df = pd.DataFrame(angles_calcs,
                                     columns=angles_colmn)
        test_angle_df.index = xyz_index_list

    if comp_dihedrals:
        test_dihedral_df = pd.DataFrame(dihedral_calcs,
                                     columns=dihedrals_colmn)
        test_dihedral_df.index = xyz_index_list

    if comp_distances and comp_angles and comp_dihedrals:
        frames = [test_dist_df, test_angle_df, test_dihedral_df]

    elif comp_distances and comp_angles:
        frames = [test_dist_df, test_angle_df]

    elif comp_distances and comp_dihedrals:
        frames = [test_dist_df, test_dihedral_df]

    elif comp_angles and comp_dihedrals:
        frames = [test_angle_df, test_dihedral_df]

    elif comp_distances:
        frames = [test_dist_df]

    elif comp_angles:
        frames = [test_angle_df]

    elif comp_dihedrals:
        frames = [test_dihedral_df]

    calculations_df = pd.concat(frames, axis=1)
    specific_file_object.close()
    return calculations_df
    # return test_xyz_df,test_dist_df,test_angle_df,test_dihedral_df,calculations_df
