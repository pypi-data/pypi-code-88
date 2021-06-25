# Create dataframe with xyz contents
import pandas as pd
import numpy as np
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


#  Goal 1: Grab XYZ Content


def xyz_contents(xyz_files, user_directory):
    xyz_index_list = []
    comp_distances = False
    comp_angles = False
    comp_dihedrals = False

    while True:
        try:
            complete_path = user_directory + "/" + xyz_files[0]
            specific_file_object = open(complete_path)
            n_atoms_distangdih = specific_file_object.readline()
            n_atoms_distangdih = int(n_atoms_distangdih)

            atoms_list = list(range(1, n_atoms_distangdih + 1))

            print("Which atoms you would like to compute calculations on.")
            print("All you need to type is the atom NUMBER, no spaces (ex. 1,5,7,8,10)")
            print("If you would like all, enter 'all'")

            userAtomsChoice = input("Atoms: ")

            if userAtomsChoice == "all":
                atomsChoice = list(range(1, n_atoms_distangdih + 1))

            else:
                #  remove duplicates using set()
                split_Choices = userAtomsChoice.split(",")

                # removing any possible empty strings
                # https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
                split_Choices = list(filter(None, split_Choices))

                atomsChoice = list(map(int, set(split_Choices)))
                atomsChoice.sort()
                #  list(map(int, test_list) will make each number in list an int

            atoms_list = atomsChoice

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
                dihedral_indexes_list = []

                for atom_1 in atoms_list:

                    for atom_2 in atoms_list:
                        if atom_2 != atom_1:

                            for atom_3 in atoms_list:
                                if atom_3 > atom_2 and atom_3 != atom_1:

                                    for atom_4 in atoms_list:

                                        if atom_4 not in [atom_1, atom_2, atom_3] and atom_4 > atom_1:
                                            dihedral_indexes_list.append([atom_1, atom_2, atom_3, atom_4])

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

            # current_index = 0
            # atom_index = n_atoms * 3
            # while current_index < atom_index:
            #     if current_index/3 in atoms_list: #or (current_index/3)+1 in atoms_list:
            #         print(current_index)
            #         print(current_index/3)
            #         print(current_index+1)
            #         print("NEWWWWWWW")
            #         print()
            #
            #
            #         # a1 is the coordinates for one atom; three indices used in temp_xyz_contents to describe one atom
            #         a1 = [float(temp_xyz_contents_list[current_index]),
            #               float(temp_xyz_contents_list[current_index + 1]),
            #               float(temp_xyz_contents_list[current_index + 2])]
            #
            #         index_iteration = current_index + 3  # overall would be index 3 in the first loop
            #         #  index 3 would be the x-coord of a new atom
            #         a1_array = np.array(a1)
            #
            #     else:
            #         current_index = current_index + 3
            #         continue
            #
            #     while index_iteration < atom_index:  # same check as first while, but will catch last index
            #         if index_iteration / 3 in atoms_list or index_iteration + 1 in atoms_list:
            #             a2 = [float(temp_xyz_contents_list[index_iteration]),
            #                   float(temp_xyz_contents_list[index_iteration + 1]),
            #                   float(temp_xyz_contents_list[index_iteration + 2])]
            #
            #             a2_array = np.array(a2)
            #             v1 = a2_array-a1_array
            #             dist = np.linalg.norm(v1)
            #             temp_dist_list.append(dist)
            #             dist_colname_list.append(temp_xyz_colname_list[current_index][:-2] +
            #                                      "to " + temp_xyz_colname_list[index_iteration][:-2])  # Ex. 15 C to 18 H
            #
            #             index_iteration = index_iteration + 3
            #
            #         else:
            #             index_iteration = index_iteration + 3
            #             continue
            #
            #     current_index = current_index + 3


        # ANGLES
        # Getting Angles from each atom to all others

        if comp_angles:
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
                                         "to " + temp_xyz_colname_list[3 * angle_list[1] - 1][:-2]+
                                         "to " + temp_xyz_colname_list[3 * angle_list[2] - 1][:-2])  # Ex. 15 C to 18 H

            master_angle_contents_list.append(temp_angle_list)
            print("Angles: COMPLETE")

            # current_index = 0
            # atom_index = n_atoms*3
            #
            # while current_index < atom_index:
            #     if current_index / 3 in atoms_list or current_index + 1 in atoms_list:
            #         index_iteration = 0
            #
            #         a1 = [float(temp_xyz_contents_list[current_index]),
            #               float(temp_xyz_contents_list[current_index+1]),
            #               float(temp_xyz_contents_list[current_index+2])]
            #         a1_array = np.array(a1)
            #
            #     else:
            #         current_index = current_index+3
            #         continue
            #
            #     while index_iteration < atom_index:
            #
            #         if index_iteration == current_index:  #  ensures no index angle can be compared to itself
            #             index_iteration = index_iteration+3
            #             continue
            #
            #         elif index_iteration / 3 in atoms_list or index_iteration + 1 in atoms_list:
            #             index_iteration2 = 0
            #
            #             a2 = [float(temp_xyz_contents_list[index_iteration]),
            #                   float(temp_xyz_contents_list[index_iteration + 1]),
            #                   float(temp_xyz_contents_list[index_iteration + 2])]
            #             a2_array = np.array(a2)
            #
            #             v1 = a2_array - a1_array
            #
            #         else:
            #             index_iteration = index_iteration + 3
            #             continue
            #
            #         #  Now get v2
            #         while index_iteration2 < atom_index:
            #             if index_iteration2 == index_iteration or index_iteration2 == current_index or index_iteration2 > index_iteration:
            #                 index_iteration2 = index_iteration2 + 3 #same as above, no comparison to self
            #                 continue
            #
            #             elif index_iteration2 / 3 in atoms_list or index_iteration2 + 1 in atoms_list:
            #                 a3 = [float(temp_xyz_contents_list[index_iteration2]),
            #                       float(temp_xyz_contents_list[index_iteration2 + 1]),
            #                       float(temp_xyz_contents_list[index_iteration2 + 2])]
            #                 a3_array = np.array(a3)
            #
            #                 v2 = a3_array - a2_array
            #                 da = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))  # in radians
            #                 da_degrees = np.degrees(da)
            #                 temp_angle_list.append(da_degrees)
            #                 angle_colname_list.append(temp_xyz_colname_list[current_index][:-2] +
            #                                           "to " + temp_xyz_colname_list[index_iteration][:-2] +
            #                                           "to " + temp_xyz_colname_list[index_iteration2][:-2])
            #                 # Ex. 15 C to 18 H to 20 F
            #                 index_iteration2 = index_iteration2 + 3
            #
            #             else:
            #                 index_iteration2 = index_iteration2 + 3
            #                 continue
            #
            #         index_iteration = index_iteration + 3
            #
            #     current_index = current_index+3



        # Dihedrals
        # Getting Dihedrals from each atom to all others
        if comp_dihedrals:
            temp_dihedral_list = []
            dihedral_colname_list = []

            # current_index = 0
            # atom_index = n_atoms*3
            #
            # while current_index < atom_index:
            #     index_iteration = 0
            #
            #     a1 = [float(temp_xyz_contents_list[current_index]),
            #           float(temp_xyz_contents_list[current_index+1]),
            #           float(temp_xyz_contents_list[current_index+2])]
            #     a1_array = np.array(a1)
            #
            #     while (index_iteration < atom_index):
            #         index_iteration2 = 0
            #
            #         if(index_iteration == current_index):  #  ensures no index angle can be compared to itself
            #             index_iteration = index_iteration+3
            #             continue
            #
            #         else:
            #             a2 = [ float(temp_xyz_contents_list[index_iteration]),
            #                    float(temp_xyz_contents_list[index_iteration+1]),
            #                    float(temp_xyz_contents_list[index_iteration+2])]
            #             a2_array = np.array(a2)
            #
            #             v1 = a2_array-a1_array
            #
            #             #  Now get v2
            #             while(index_iteration2 < atom_index):
            #                 index_iteration3 = 0
            #
            #                 if(index_iteration2 == index_iteration or index_iteration2 == current_index):
            #                     index_iteration2 = index_iteration2 + 3 #same as above, no comparison to self
            #                     continue
            #
            #                 else:
            #
            #                     a3 = [float(temp_xyz_contents_list[index_iteration2]),
            #                           float(temp_xyz_contents_list[index_iteration2 + 1]),
            #                           float(temp_xyz_contents_list[index_iteration2 + 2])]
            #                     a3_array = np.array(a3)
            #
            #                     v2 = a3_array - a2_array
            #                     n1 = np.cross(v1,v2) #  cross product
            #
            #                     while index_iteration3 < atom_index:
            #                         if(index_iteration3 == index_iteration or index_iteration3 == index_iteration2 or
            #                         index_iteration3 == current_index):
            #                             index_iteration3 = index_iteration3 + 3
            #                             continue
            #
            #                         else:
            #                             a4 = [float(temp_xyz_contents_list[index_iteration3]),
            #                                   float(temp_xyz_contents_list[index_iteration3 + 1]),
            #                                   float(temp_xyz_contents_list[index_iteration3 + 2])]
            #                             a4_array = np.array(a4)
            #
            #                             v3 = a2_array - a3_array
            #                             v4 = a4_array - a3_array
            #                             n2 = np.cross(v3,v4)
            #
            #                             dihedral = np.arccos(np.round(-np.dot(n1, n2) /
            #                                                           (np.linalg.norm(n1) *
            #                                                            np.linalg.norm(n2)), decimals=4)) #rads
            #
            #                             # dihedral = np.arccos(-np.dot(n1, n2)/(np.linalg.norm(n1)*np.linalg.norm(n2))) # rads
            #
            #                             # Hold for demonstration on friday: to revert code, all you need
            #                             # to do is to remove the np.round part (and decimals =) to show how the rounding
            #                             # was messing up everything
            #                             # if math.isnan(dihedral):
            #                             #     print("n1:", n1)
            #                             #     print("n2:", n2)
            #                             #     print("dihedral:",dihedral)
            #                             #     print("dotproduct n1n2:",-np.dot(n1,n2))
            #                             #     print("n1 norm:",np.linalg.norm(n1))
            #                             #     print("n2 norm:",np.linalg.norm(n2))
            #                             #
            #                             #     print("not rounded:",-np.dot(n1,n2)/(np.linalg.norm(n1)*np.linalg.norm(n2)))
            #                             #     print(np.round(-np.dot(n1,n2)/(np.linalg.norm(n1)*np.linalg.norm(n2)),decimals=3))
            #                             #     sys.exit()
            #                             #     break
            #
            #                             if np.dot(n1,v4) > 0:
            #                                 dihedral = -1*dihedral
            #
            #                             dihedral_degrees = np.degrees(dihedral)
            #
            #                             #MODIFICATION OF DIHEDRALS (NO LONGER ACTUAL DIHEDRALS)
            #                             if dihedral_degrees > 90 and dihedral_degrees < 180:
            #                                 dihedral_degrees = 180 - dihedral_degrees
            #
            #                             elif dihedral_degrees < -90 and dihedral_degrees > -180:
            #                                 dihedral_degrees = -180-dihedral_degrees
            #
            #                             #  Its important to note that dihedrals have been modified to
            #                             #  ensure PCA treats dihedrals of different sinage similarly
            #                             #  we want PCA to know that the maximal difference in dihedrals
            #                             #  is dependent on whether or not a dihedral is close to 90 degrees
            #
            #                             temp_dihedral_list.append(dihedral_degrees)
            #
            #                             dihedral_colname_list.append(temp_xyz_colname_list[current_index][:-2] +
            #                                                          "to " + temp_xyz_colname_list[index_iteration][:-2] +
            #                                                          "to " + temp_xyz_colname_list[index_iteration2][:-2] +
            #                                                          "to " + temp_xyz_colname_list[index_iteration3][:-2])
            #                             # Ex. 1 C to 12 H to 20 F to 21 C
            #
            #                             index_iteration3 = index_iteration3 +3
            #
            #                 index_iteration2 = index_iteration2 + 3
            #
            #
            #             index_iteration = index_iteration + 3
            #
            #     current_index = current_index+3
            # master_dihedral_contents_list.append(temp_dihedral_list)

            for di_list in dihedral_indexes_list:
                a1 = [float(temp_xyz_contents_list[3*di_list[0]-3]),
                      float(temp_xyz_contents_list[3*di_list[0]-2]),
                      float(temp_xyz_contents_list[3*di_list[0]-1])]
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


                dihedral = np.arccos(np.round(-np.dot(n1, n2)/(np.linalg.norm(n1) * np.linalg.norm(n2)), decimals=4))
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

                dihedral_colname_list.append(temp_xyz_colname_list[3 * di_list[0]-1][:-2] +
                                             "to " + temp_xyz_colname_list[3 * di_list[1]-1][:-2] +
                                             "to " + temp_xyz_colname_list[3 * di_list[2]-1][:-2] +
                                             "to " + temp_xyz_colname_list[3 * di_list[3]-1][:-2])
                # Ex. 1 C to 12 H to 20 F to 21 C
            master_dihedral_contents_list.append(temp_dihedral_list)

            print("Dihedrals: COMPLETE")
            print()
            print()

    test_xyz_df = pd.DataFrame(master_xyz_contents_list,
                               columns=temp_xyz_colname_list)
    test_xyz_df.index = xyz_index_list


    if comp_distances:
        test_dist_df = pd.DataFrame(master_dist_contents_list,
                                    columns=dist_colname_list)
        test_dist_df.index = xyz_index_list

    if comp_angles:
        test_angle_df = pd.DataFrame(master_angle_contents_list,
                                     columns=angle_colname_list)
        test_angle_df.index = xyz_index_list

    if comp_dihedrals:
        test_dihedral_df = pd.DataFrame(master_dihedral_contents_list,
                                     columns=dihedral_colname_list)
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
