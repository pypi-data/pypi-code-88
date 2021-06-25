import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
# import plotly.tools as tls
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D #needed for 3D visualizations

import pca_creation
# column_headers = ["1 C to 2 H", "1 C to 3 H", "1 C to 4 C", "17 H to 16 H to 15 H to 12 H",
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
#
# print(test_df.iloc[:,:2])
# print(test_df.index[0][:-6])

def clustering_model(pca_df,num_PCA_components,original_df):

    print("Clustering Analysis on PCA data commencing...")
    print("Clustering will be done on 1-10 clusters")

    kclusters = range(1,11)

    inertias = []
    #  we keep a list of all intertias for each model of clustering to see which one is the most accurate

    for k in kclusters:
        # create model and fit to data
        model = KMeans(n_clusters=k)
        model.fit(pca_df)
        inertias.append(model.inertia_)
        # inertia_ (kmeans attribute): Sum of squared distances of samples to their closest cluster center.

    # Method 1 for plotting inertias
    # plt.plot(kclusters, inertias, '-o', color='black')
    # plt.xlabel('number of clusters, k')
    # plt.ylabel('inertia')
    # plt.xticks(kclusters)
    # plt.show()
    # print(inertias)
    # print(kclusters)

    ten_clusters = []
    for i in range(1,11):
        ten_clusters.append(i)

    # print("CLUSTERRR:",ten_clusters)
    # print(inertias)
    # df_inertias = pd.DataFrame([inertias,ten_clusters]).transpose()
    # df_inertias.columns = ["Inertia","Number of Clusters"]
    # df_inertias.index += 1
    # print(df_inertias)

    # method 2 for showing inertia plot
    # fig1 = px.line(df_inertias, x="Number of Clusters",y="Inertia")
    # fig1.show()

    figtest = go.Figure()
    figtest.add_trace(go.Scatter(x=ten_clusters,y=inertias))
    figtest.update_layout(title='Inertias for choosing best number of clusters',
                      xaxis_title='Number of Clusters',
                      yaxis_title='Inertia')

    figtest.show()
    # inertias_np = np.array(inertias)
    # data1 = pgo.Scatter(x=kclusters,
    #         y=inertias_np)
    # layout1 = pgo.Layout(title="Inertias for choosing best number of clusters",
    #                      xaxis="Number of clusters",yaxis="Inertia")
    # fig1a = pgo.Figure(data1,layout1)
    # fig1a.show()


    #do the math to get the 'best' cluster
    # then tell em what it is but still allow user to choose # clusters


    print("After seeing the elbow point graph, how many clusters will you like to conduct for your data")
    user_clusters = int(input("Desired Clusters: "))
    print()
    print("Desired number of clusters received")

    user_Kmeans = KMeans(n_clusters= user_clusters)
    user_Kmeans.fit(pca_df)
    labels = user_Kmeans.predict(pca_df) # K means predicting the family
    centroids = np.array(user_Kmeans.cluster_centers_)

    families = []
    for integer in labels:
        integer+=1
        families.append("Family "+str(integer))   # creates the labeling of the graph look nicer, not just a number

    #Create dataframe containing pca data + families
    df_columns = []
    for num in range(1,num_PCA_components+1):
        df_columns.append("PC "+str(num))

    pca_df_final = pd.DataFrame(pca_df, columns= df_columns)

    pca_df_final["Families"] = families
    pca_df_final.index = original_df.index

    #Create dataframe containing centroids
    centroids_df = pd.DataFrame(user_Kmeans.cluster_centers_,columns=df_columns)

    if num_PCA_components == 2:
        fig2 = px.scatter(pca_df_final, x="PC 1", y="PC 2",
                          title='2D Clustering',
                          hover_name=pca_df_final.index,
                          size_max=0.1,
                          color="Families")

        fig2.add_trace(go.Scatter(x=centroids_df["PC 1"], y=centroids_df["PC 2"],
                                  name="Centroid",
                                  mode="markers",
                                  marker_color='rgba(2, 2, 2, 2)'))
        fig2.show()

        # trace0 = pgo.Scatter(x=pca_df_final["PC 1"],
        #              y=pca_df_final["PC 2"],
        #              text=pca_df_final.index,
        #              name='')
        #              # mode='markers',
        #              # marker=pgo.Marker(size=df['tpop10'],
        #              #                   sizemode='diameter',
        #              #                   sizeref=df['tpop10'].max()/50,
        #              #                   opacity=0.5,
        #              #                   color=Z),
        #              # showlegend=False)
        #
        # trace1 = pgo.Scatter(x=user_Kmeans.cluster_centers_[:, 0],
        #                      y=user_Kmeans.cluster_centers_[:, 1],
        #                      name='',
        #                      mode="markers",
        #                      marker=pgo.Marker(symbol='x'))
        #
        # data7 = pgo.Data([trace0, trace1])
        # layout7 = layout5
        # layout7['title'] = 'Baltimore Vital Signs (PCA and k-means clustering with 7 clusters)'
        # fig7 = pgo.Figure(data=data7, layout=layout7)



    elif num_PCA_components == 3:
        fig3 = px.scatter_3d(pca_df_final, x="PC 1", y="PC 2", z="PC 3",
                             title='3D Clustering',
                             hover_name=pca_df_final.index,
                             color="Families",
                             size_max=0.1)

        fig3.add_trace(go.Scatter(x=centroids_df["PC 1"], y=centroids_df["PC 2"],z=centroids_df["PC 3"],
                                  name="Centroid",
                                  mode="markers",
                                  marker_color='rgba(2, 2, 2, 2)'))
        fig3.show()

    else:
        print("You have asked for a not-optimal number of components for visualization ( >3 dimensions ) ")
        print("Each structure and their corresponding family has been printed in the terminal")

        #change to families.csv #### do this!!!
        # file_family_name = input("What would you like your csv file name?")
        file_family_name = pca_df_final.index[0][:-6] # will cut off _#.xyz from file name; might remove bc maybe not
                                                # everyone has that naming convention

        #take out just .xyz or something; split off of the "." and take everything to the left of it

        pca_df_final.to_csv(file_family_name+"_families.csv")

    print(pca_df_final)

    return pca_df_final,user_clusters


# def clustering_model(pca_df):
#
#     print("Clustering Analysis on PCA data commencing...")
#     print("Clustering will be done on 2-10 clusters")
#
#     kclusters = range(2,11)
#     RSSs = []
#     #we keep a list of all RSS's for each model of clustering to see which one is the most accurate
#
#     for k in kclusters:
#         # create model and fit to data
#         kmeans, z = cluster(i)
#         model = KMeans(n_clusters=k)
#         model.fit(pca_df)
#         RSSs.append(model.inertia_)
#         # inertia_ (kmeans attribute): Sum of squared distances of samples to their closest cluster center.
#
#     plt.plot(kclusters, RSSs, '-o', color='black')
#     plt.xlabel('number of clusters, k')
#     plt.ylabel('inertia')
#     plt.xticks(kclusters)
#     plt.show()
#
#     return plt.show()
#
# kclusters = range(2, 11)
# RSSs = []
# # we keep a list of all RSS's for each model of clustering to see which one is the most accurate
#
# for k in kclusters:
#     # create model and fit to data
#     model = KMeans(n_clusters=k)
#     model.fit(X)
#     RSSs.append(model.inertia_)
#     # inertia_ (kmeans attribute): Sum of squared distances of samples to their closest cluster center.
#
# plt.plot(kclusters, RSSs, '-o', color='black')
# plt.xlabel('number of clusters, k')
# plt.ylabel('inertia')
# plt.xticks(kclusters)
# plt.show()
#
# print("After seeing the elbow point graph, how many clusters will you like to conduct for your data")
# user_clusters = int(input("Desired Clusters: "))
#
# user_Kmeans = KMeans(n_clusters= user_clusters)
# user_Kmeans.fit(X)
# labels = user_Kmeans.predict(X)
#
# centroids = user_Kmeans.cluster_centers_
# u_labels = np.unique(labels)
#
# print(labels)
# print(centroids)
#
# plt.scatter(X[:,0], X[:,1], c =labels, cmap="viridis")
# plt.scatter(centroids[:,0], centroids[:,1], s=80, color='black', alpha=0.5)
# plt.legend()
# plt.show()

