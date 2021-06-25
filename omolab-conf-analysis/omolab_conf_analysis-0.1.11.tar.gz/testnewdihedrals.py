#
# atoms = 5
#
# atom_list = [1,2,3,4,5]
# # print(atom_list[:3])
#
# plane1 = []
# plane2 = []
#
# print()
# #take first three, add it to plane1, take last three, add it to plane two
# plane1.append(atom_list[:3])
# plane2.append(atom_list[1:4])
#
# plane1.append(atom_list[:3])
# plane2.append(atom_list[1:3] +[atom_list[4]])
#
# print("Current Planes")
# print(plane1)
# print(plane1[0])
# print()
# print(plane2)
# print(plane2[0])
#
#
# print("Planes to avoid")
# plane1_avoid = []
# plane2_avoid = []
#
# plane1_avoid.append(plane2[0][::-1]) #  reverse
# plane2_avoid.append(plane1[0][::-1]) #  reverse
#
# plane1_avoid.append(plane2[1][::-1]) #  reverse
# plane2_avoid.append(plane1[1][::-1]) #  reverse
#
# print(plane1_avoid)
# print(plane2_avoid)
#
# #[1 3 2 ] [3 2 5] same as [1 2 3] [2 3 5]
# print("tesdre")
#
# print(plane1)
# plane1_avoid.append((plane1[1][1],plane1[1][2] = plane1[1][2],plane1[1][1]))
# plane2_avoid.append((plane2[1][0],plane2[1][1] = plane2[1][1],plane2[1][0]))
# print(plane1)
# print(plane2)
# #plane2.append(atom_list[-4:2] +
# print()
#
# print(plane1_avoid)
# print(plane2_avoid)
#
# """
# 1 2 3 not 1 3 2
#                     second list
#                     2 3 1 can this be done? no; should not be done because 1 in first list
#                     2 3 2 no work should not be done because 1 in first list ++ more
#                     2 3 3 no work should not be done because 1 in first list ++ more
#                     2 3 4
#                     2 3 5
#                     (not 2 4 3 should not be done because 4 > 3 and first two indeces are not 2 3)
#                     (not 2 5 3 should not be done because 5 > 3 and first two indeces are not 2 3)
# 1 2 4
# 1 2 5
#
#
# 1 3 4
# 1 3 5
#
# 1 4 5
#
#
# 2 1 3 not 2 3 1
# 2 1 4
# 2 1 5
#
# 2 2 no work
#
# 2 3 1 should not be done because 3 > 1 (ie 2 1 3 has been done)
# 2 3 2 no work
# 2 3 4
# 2 3 5
#
# 2 4 1 should not be done because 4 > 1
# 2 4 2 no work
# 2 4 3 should not be done because 4 > 3
# 2 4 4 no work
# 2 4 5
#
# 3 1 2 not 3 2 1
# 3 1 3
# 3 1 4
# 3 1 5
#
# 3 2 1 should not be done because 2 > 1
# 3 2 2 no work
# 3 2 3 no work
# 3 2 4
# 3 2 5
#
# 3 3 no work
#
# 3 4 1 should not be done because 4 > 1
# 3 4 2 should not be done because 4 > 2
# 3 4 3 no work
# 3 4 4 no work
# 3 4 5
#                 second list
#                     4 5 1
#                     4 5 2
#                     4 5 3 no work should not be done because 1 in first list ++ more
#                     4 5 4 no
#                     4 5 5 no
#
#
#
# ...
#
# 5 1 2
# 5 1 3
# 5 1 4
# 5 1 5 no work
#
# 5 2 1 should not be done because 2 > 1 (ie 5 1 2)
# ...
#
# 5 4 3 should not be done because 4 > 3 (ie 3 4 5)
# """
#
# #Trying to think lol
# """
# input: number of atoms
# output: two lists of lists -->
#         list 1 = list of lists where each index contains the atom #/index to be in the plane
#         (ex. [5 1 2] is atom 5 atom 1 and atom 2
#
#         list 2 = list of lists where each index contains the atom #/index to be in the plane
#                 --> index matches with list 1 index
#
#         thus the first dihedrals calculated will be from
#         list1[0] and list2[0], then
#         list1[1] and list2[1] etc.
#
#         list1 = []
#         list2 = []
#         num_atoms = 5
#         atoms_list -> [1, 2, 3, 4, 5] #figure out how to generate
#         atoms_list = [1:num_atoms]
#         #first list
#         for atom_1 in atoms_list:
#
#             for atom_2 in atoms_list:
#
#                 if atom2 != atom1:
#
#                     for atom_3 in atoms_list:
#                         if atom3 > atom2 and atom3 != atom1:
#
#                             for atom_4 in num_atoms:
#                                 if atom_4 not in [atom_1, atom_2, atom_3]:
#                                     list1.append([atom1, atom2, atom3, atom4])
#                                     # list2.append([atom2,atom3,atom4])
#
#                     at the end list1 and list2 contain all the necessary pairs for dihedrals
#
#
#                     #Dihedrals
#                     for firstl, secondl in zip(list1, list2): #zip allows us to iterate through two lists simultaneously
#                         atom1 = tempxyzlist
#
#                         a1 = [float(temp_xyz_contents_list[3*firstl[0]-2]),
#                                   float(temp_xyz_contents_list[3*firstl[0]-1]),
#                                   float(temp_xyz_contents_list[3*firstl[0]])]
#                         a1_array = np.array(a1)
#
#                         a2 = [float(temp_xyz_contents_list[3*firstl[1]-2]),
#                                   float(temp_xyz_contents_list[3*firstl[1]-1]),
#                                   float(temp_xyz_contents_list[3*firstl[1]])]
#                         a2_array = np.array(a2)
#
#                         a3 = [float(temp_xyz_contents_list[3*firstl[2]-2]),
#                                   float(temp_xyz_contents_list[3*firstl[2]-1]),
#                                   float(temp_xyz_contents_list[3*firstl[2]])]
#                         a3_array = np.array(a3)
#
#                         a4 = [float(temp_xyz_contents_list[3*firstl[3]-2]),
#                                   float(temp_xyz_contents_list[3*firstl[3]-1]),
#                                   float(temp_xyz_contents_list[3*firstl[3]-2])]
#                         a4_array = np.array(a4)
#
#                         v1 = a2_array-a1_array
#                         v2 = a3_array - a2_array
#                         n1 = np.cross(v1,v2) #  cross product
#                         v3 = a2_array - a3_array
#                         v4 = a4_array - a3_array
#                         n2 = np.cross(v3,v4)
#
#                         dihedral = np.arccos(np.round(-np.dot(n1, n2) /
#                                           (np.linalg.norm(n1) *
#                                            np.linalg.norm(n2)), decimals=4)) #rads
#
#                         if np.dot(n1,v4) > 0:
#                             dihedral = -1*dihedral
#
#                         dihedral_degrees = np.degrees(dihedral)
#
#                         #MODIFICATION OF DIHEDRALS (NO LONGER ACTUAL DIHEDRALS)
#                         if dihedral_degrees > 90 and dihedral_degrees < 180:
#                             dihedral_degrees = 180 - dihedral_degrees
#
#                         elif dihedral_degrees < -90 and dihedral_degrees > -180:
#                             dihedral_degrees = -180-dihedral_degrees
#
#
#                         temp_dihedral_list.append(dihedral_degrees)
#
#                         dihedral_colname_list.append(temp_xyz_colname_list[3*firstl[0]][:-2] +
#                                                                                  "to " + temp_xyz_colname_list[3*firstl[1]][:-2] +
#                                                                                  "to " + temp_xyz_colname_list[3*firstl[2]][:-2] +
#                                                                                  "to " + temp_xyz_colname_list[3*firstl[3]][:-2])
#                                                     # Ex. 1 C to 12 H to 20 F to 21 C
#
#                     master_dihedral_contents_list.append(temp_dihedral_list)
#
#
#
#
# """
#
#
#
#
#
#
# # for combinations in atom_list:

test = [[1, 2 ,3],[3,2,1]]
print(test)

for list in reversed(test):
    if list[::-1] in test:
        print(list)
        test.remove(list)


print(test)

