from sklearn.decomposition import PCA
import numpy as np
import plotly.express as px
import pandas as pd
import os

# column_headers = [" 1 C to 2 H", "1 C to 3 H", "1 C to 4 C", "17 H to 16 H to 15 H to 12 H",
#                "17 H to 16 H to 15 H to 13 H", "17 H to 16 H to 15 H to 14 C"]
#
# indexes = ["pentane_1.xyz", "pentane_3.xyz", "pentane_2.xyz", "pentane_4_fake.xyz", "pentane_5_fake.xyz"]
#
#
# A = np.array([[1.096276,1.096276,1.528389,55.236766,71.552750,37.123885],
#               [1.096818,1.095462,1.530606,121.597386,100.494262,37.106736],
#               [1.097144,1.095743,1.531324,67.610414,128.966981,37.456963],
#               [1.530606,1.095462,1.196818,121.106736,100.966981,37.530606],
#               [128.966981,1.095743,1.531324,37.456963,1.097144,67.610414]])
#
#
# test_df = pd.DataFrame(A, columns=column_headers)
# test_df.index = indexes
# print(test_df)
# print(test_df.shape[0])



###need to create try catch block with input of  user PCs
# if the user asks for too high of pc then kick them back to the top of the while or for loop and renter number
# if user ask >= test_df.shape[0], then change it jackass!!!

class InvalidUserEntranceError(Exception):
    def __init__(self, message):
        self.message = message


def pca_model(user_input_pca,dataframe):
    model = PCA(n_components=user_input_pca)
    print()
    print("______________________________________________________")
    print("Model created with {} principal component(s)".format(user_input_pca))
    print("Default plots to be shown")
    print("______________________________________________________")
    num_components = user_input_pca
    components = model.fit_transform(dataframe)
    # print(components)
    size_dots = dataframe.shape[0]*[float(00000.1)]
    size_dots = range(1,23)

    #Explained Variance Plot
    explained_variance = np.cumsum(model.explained_variance_ratio_)
    fig1 = px.area(x = range(1, explained_variance.shape[0] + 1), y = explained_variance,
                   labels={"x": "Number of Components", "y":"Explained Variance"})

    fig1.show() #BE SURE TO UNCOMMENT AT END

    if  user_input_pca == 2:
        # Scatter Plot
        fig2 = px.scatter(components, x=0, y=1, hover_name=dataframe.index, labels={"0": "PC 1", "1": "PC 2"},size_max=0.1)#, size = size_dots)
        fig2.show()

    elif user_input_pca == 3:
        total_var = model.explained_variance_ratio_.sum() * 100

        pca_labels = {str(i): f"PC {i + 1} ({var:.1f}%)" for i, var in enumerate(model.explained_variance_ratio_ * 100)}
        fig3 = px.scatter_matrix(components, labels=pca_labels,
                                 dimensions= range(user_input_pca),
                                 hover_name=dataframe.index, size_max=0.1)#,
                                 #size=size_dots)
        fig3.update_traces(diagonal_visible = False)
        fig3.show()

        fig4 = px.scatter_3d(components, x=0, y=1, z=2,
                             title=f'Total Explained Variance: {total_var:.2f}%',
                             labels= {"0": "PC 1", "1": "PC 2", "2": "PC 3"},
                             hover_name=dataframe.index,size_max=0.1)#,
                             #size=size_dots)
        fig4.show()

    else:
        print("You have asked for a not-optimal number of components for visualization ( >3 dimensions ) ")
        total_var = model.explained_variance_ratio_.sum() * 100

        pca_labels = {str(i): f"PC {i + 1} ({var:.1f}%)" for i, var in enumerate(model.explained_variance_ratio_ * 100)}
        fig3 = px.scatter_matrix(components, labels=pca_labels,
                                 dimensions= range(user_input_pca),
                                 hover_name=dataframe.index,
                                 title=f'Total Explained Variance: {total_var:.2f}%',
                                 )
        fig3.update_traces(diagonal_visible = False)
        fig3.show()

    attempts_left = 10
    for attempt in range(10):  # user has ten times to get a correct num of pcs desired, otherwise must restart
        try:
            print()
            print("Would you like to see which features in the original dataset contribute the most to a chosen PC?")

            feature_importance_test = input("Enter Y/N: ").upper()

            while feature_importance_test != "Y" and feature_importance_test != "N":
                raise InvalidUserEntranceError("You did not choose Y or N, try again.")

            if feature_importance_test == "Y":
                continue_feature_insights = True

                while continue_feature_insights:
                    print("Which Principal Component would you like to test?")
                    test_PC = int(input("PC #: "))

                    while test_PC > user_input_pca:
                        raise InvalidUserEntranceError("Error; PC not calculated due to previous input response. Try Again")

                    print()
                    print("PC Noted--Finding Feature Importance")
                    print("The top 10 features with the largest influcence on PC", test_PC, "will be printed")
                    print()

                    # model.components_ are the loadings, which give a magnitude and direction on the PC given
                    # model.components_[test_PC - 1] --> list of components

                    loading_scores = pd.Series(model.components_[test_PC - 1],
                                               index=dataframe.columns.tolist())

                    sorted_loading_scores = loading_scores.abs().sort_values(
                        ascending=False)  # contains all loading scores

                    top10_features = sorted_loading_scores[0:10].index.values

                    print("Top 10 Features and their given magnitude and direction")
                    print(loading_scores[top10_features])
                    print()
                    print("Would you like to stop?")
                    user_stop_feat = input("Enter Y/N: ").upper()

                    if user_stop_feat == "Y":
                        continue_feature_insights = False

            else:
                print()
                print("You chose not to see the features, continuing...")

            print("No longer seeing features, continuing...")

        except InvalidUserEntranceError as e:
            print()
            print(e.message)
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

        break

    return components,num_components,dataframe

#  dataframe = original dataframe
