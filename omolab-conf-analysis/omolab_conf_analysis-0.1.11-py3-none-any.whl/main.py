import os
import xyz_old_version
import xyz
import pca_creation
import pymol
import clustering
import stat
from datetime import datetime

startTime = datetime.now()
print(startTime)
print("What is the directory in which your xyz files are in?")

class PathNoExistError(Exception):
    def __init__(self, message):
        self.message = message


class NoXYZFileExistError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidPCAError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidClusterError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidUserEntranceError(Exception):
    def __init__(self, message):
        self.message = message


attempts_left = 10
for attempt in range(10):  # user has ten times to get a correct path, otherwise must restart
    try:
        user_input_directory = input("XYZ File Directory Path: ")
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/cycloheptadecane_file_test2"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/cycloheptadecane_file_test"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/cyclooctane_file_test"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/pentane_file_test"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/xyz_file_test"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/1_4_dioxepane_file_test"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/1fluoro4propylcyclohexane"
        # user_input_directory = "/Users/matthewnwerem/Chapman University/OMO Research Group - Project Conf. Analysis - Nwerem - proj_conf_analysis/Code Versions/Conformational_Analysis/cis_1fluoro4propylcyclohexane"


        # 1,4,7,9,12,14,18,21,24,27,30,33,36,39,42,45,46
        while not os.path.exists(user_input_directory):
            raise PathNoExistError("Path: '{}' does not exist".format(user_input_directory))

        print("______________________________________________________")
        print(user_input_directory)
        print("Path Received")
        print("______________________________________________________")

        directory_files = os.listdir(user_input_directory)
        xyz_files = []

        for file in directory_files:
            if file.endswith(".xyz"):
                xyz_files.append(file)

        if not xyz_files:  # means if the list is empty (using implicit booleanness of empty lists)
            raise NoXYZFileExistError("There are no XYZ files in the path '{}".format(user_input_directory))

        # print("Current Test XYZ File:", xyz_files[0]) #0 because first index of a LIST
        # print("Type w/ [0]", type(xyz_files[0]))
        # print("Type w/o [0]", type(xyz_files))

        # print(xyz_files)
        # complete_path = user_input_directory+"/"+xyz_files[0] #need complete path to open file
        # specific_file_object = open(complete_path)  # will need to make loop for each xyzfile when doing multiple i think

        xyz_df = xyz.xyz_contents(xyz_files, user_input_directory)
        print("______________________________________________________")
        print("Current Dataframe")
        print("Has been tested and works with")
        print("1: Adding all xyz's of t-amlyOH1.xyz from a folder to a dataframe")
        print("2: Adding a second xyz (just another copy of amylOH_1) to the same dataframe ")
        print("3: Calculating distances angles and dihedrals")
        print("4: Adding distances, angles and dihedrals to dataframe")
        print("______________________________________________________")
        print(xyz_df)
        print(datetime.now() - startTime)


    except PathNoExistError as e:
        print()
        print(e.message)
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue
    except NoXYZFileExistError as e:
        print()
        print(e.message)
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    break

attempts_left = 10
print("______________________________________________________")
print("PCA")
print("Has been tested and works with")
print("1: Creating PCA Model and its subsequent plots")
print("2: all interactive plots show correct hover name ")
print("3: showing top 10 features that effect the PC")
print("______________________________________________________")

for attempt in range(10):  # user has ten times to get a correct num of pcs desired, otherwise must restart
    try:
        testPCs = True
        while testPCs:
            userPCA_Components = input("Enter the number of components you would like to see in the model: ")
            userPCA_Components = int(userPCA_Components)

            while userPCA_Components >= xyz_df.shape[0]:
                raise InvalidPCAError("The # of components must be less than {}".format(xyz_df.shape[0]))

            userPCA_model, user_num_components,original_df = pca_creation.pca_model(userPCA_Components, xyz_df)

            print()
            print("Would you like to test with a different number of PCs?")
            testing_PCs = input("Enter Y/N: ").upper()
            print()

            if testing_PCs == "Y":
                testPCs = True

            elif testing_PCs == "N":
                testPCs = False
                print("Ending...")

            while testing_PCs != "Y" and testing_PCs != "N":
                raise InvalidUserEntranceError("You did not choose Y or N, try again.")

    except InvalidPCAError as e:
        print()
        print(e.message)
        print("Your number of components desired and dataframe dimensions do not work well for PCA")
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    except ValueError:
        print()
        print("Not an integer")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    except InvalidUserEntranceError as e:
        print()
        print(e.message)
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    break

attempts_left = 10
print("______________________________________________________")
print("Clustering")
print("Has been tested and works with")
print("1: Creating Clustering Model with PCA data and its subsequent plots")
print("2: All interactive plots show correct hover name ")
print("______________________________________________________")

for attempt in range(10):  # user has ten times to get a correct num of pcs desired, otherwise must restart
    try:
        testClusters = True
        while testClusters:
            tested_kclusters = 10

            # see if you can do it in a way where it depends on the number of conformations brought in
            # aka like change tested clusters to be half of the shape of all. That way its better
            # userPCA_model.shape[0]/2 ?? or userPCA_model.shape[0]/5?? test out and see whats best

            while tested_kclusters >= userPCA_model.shape[0]:
                raise InvalidClusterError("The # of clusters to be tested is greater than {}".format(userPCA_model.shape[0]))
                #  if this is raised, it means that you are looking into less than 10 structures
                #  in that case, it will be tougher to find differentiation anyway

            userClustermodel = clustering.clustering_model(userPCA_model, user_num_components,original_df)

            print()
            print("Would you like to test with a different number of Clusters?")
            testing_Clusters = input("Enter Y/N: ").upper()
            print()

            if testing_Clusters == "Y":
                testClusters = True

            elif testing_Clusters == "N":
                testClusters = False
                print("Ending...")

            while testing_Clusters != "Y" and testing_Clusters != "N":
                raise InvalidUserEntranceError("You did not choose Y or N, try again.")

    except InvalidClusterError as e:
        print()
        print(e.message)
        print("Your number of components desired and dataframe dimensions do not work well for PCA")
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    # except ValueError:
    #     print()
    #     print("Not an integer")
    #     attempts_left -= 1
    #     print(attempts_left, "attempts left")
    #     continue

    except InvalidUserEntranceError as e:
        print()
        print(e.message)
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    break

attempts_left = 10
os.chmod('mGenerate_PyMOL_Session.py', stat.S_IRWXU)
print("______________________________________________________")
print("Importing structures to PyMol")
print("After reviewing the given plots, which of the files would you like to view in pyMol?")
print("Enter the filename with  (ex. 'tamylOH_17.xyz'), with commas in between each name")
print("______________________________________________________")

for attempt in range(10):  # user has ten times to get a correct num of pcs desired, otherwise must restart
    try:
        pymolSession = True
        current_directory_overall = os.getcwd()

        while pymolSession:

            userPymolSession = pymol.generate_pymol(user_input_directory)
            print()
            print("Would you like to generate a PyMol Session with different structures in the current directory?")
            new_PyMolSession = input("Enter Y/N: ").upper()
            print()

            if new_PyMolSession == "Y":
                os.chdir(current_directory_overall)
                pymolSession = True

            elif new_PyMolSession == "N":
                pymolSession = False
                print("Ending...")

            while new_PyMolSession != "Y" and new_PyMolSession != "N":
                raise InvalidUserEntranceError("You did not choose Y or N, try again.")

    except InvalidUserEntranceError as e:
        print()
        print(e.message)
        print()
        print("______________________________________________________")
        attempts_left -= 1
        print(attempts_left, "attempts left")
        continue

    break






