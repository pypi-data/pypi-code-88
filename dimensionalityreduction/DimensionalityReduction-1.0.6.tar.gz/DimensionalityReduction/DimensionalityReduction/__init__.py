#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DimensionalityReduction:
    def __init__(self):
        pass
    
    def fit(self, df, target):
        self.df = df.copy()
        self.target = target
        self.cat = [i for i in df.columns if i not in df.describe().columns]
        for c in self.cat:
            self.df[c].replace(self.df[c].dropna().unique(), range(self.df[c].nunique()), inplace=True)
    
    def plot(self, plot='dash'):
        if plot == 'dash':
            fig, ax = plt.subplots(2, 2, figsize=(12, 10))
            ax = ax.flatten()
            plt.style.use('fivethirtyeight')
            plt.suptitle('Dimensionality Reduction Dash Board')
        #------------------------------%Missing------------------------------
        if plot == '%missing' or plot == 'dash':
            desc = self.df.describe().T
            desc['%missing'] = (1 - (desc['count']/len(self.df))) * 100
            
            if plot == 'dash':
                sns.barplot(
                    data=desc.sort_values('%missing', ascending=False), 
                    x='%missing', 
                    y=desc.sort_values('%missing', ascending=False).index, 
                    ax=ax[0], color='orange').set(title='%Missing'.title(), xlabel=' ')
                
            if plot != 'dash':
                fig, ax = plt.subplots(figsize=(14, 6))
                sns.barplot(
                    data=desc.sort_values('%missing', ascending=False), 
                    x='%missing', 
                    y=desc.sort_values('%missing', ascending=False).index, 
                    color='orange').set(title='%Missing'.title(), xlabel=' ')
            
            self.missing = desc['%missing'][desc['%missing'] > 95]
        #------------------------------Amount of Variation------------------------------
        if plot == 'var' or plot == 'dash':
            std_df = self.df.drop(self.target, axis=1)
            std_df = (std_df.describe().T['std'] - std_df.min())/ (std_df.max() - std_df.min())
            std_df.sort_values(ascending=False, inplace=True)   
            
            if plot == 'dash':
                sns.lineplot(
                    data=std_df, 
                    x=[i + 1 for i in range(len(std_df.index))], 
                    y=std_df.values, 
                    linewidth=2, ax=ax[1]).set(title='Amount of Variation'.title(), xlabel=' ')
                
            if plot != 'dash':
                fig, ax = plt.subplots(figsize=(14, 6))
                sns.lineplot(
                    data=std_df, 
                    x=[i + 1 for i in range(len(std_df.index))], 
                    y=std_df.values, 
                    linewidth=2).set(title='Amount of Variation'.title(), xlabel=' ')
        
        #------------------------------Multicolinearity------------------------------
        if plot == 'multico' or plot == 'dash':
            eig=[]
            for i,j in zip(self.df.isnull().sum().index, self.df.isnull().sum()):
                if j == 0:
                    eig.append(i) # Selecting columns that do not contain any NaNs and inf. values
            
            eigen_matrix = self.df[eig].corr().iloc[1:, 1:]
            w, v = np.linalg.eig(eigen_matrix) # eigen values & eigen vectors

            CI=np.round((w.max()/w)**0.5) # Condition Index
            CI_index = ['U' + str(i) + ' = ' + str(j) for i, j in zip(range(len(eigen_matrix.columns)),CI)]
            Multicolinearity_matrix=round(pd.DataFrame(v,columns=[eigen_matrix.columns],index=CI_index), 1)
            Multicolinearity_matrix.sort_index(level=1,ascending=False,inplace=True)

            cmap = sns.diverging_palette(0, 230, 90, 60, as_cmap=True)
            
            if plot == 'dash':
                sns.heatmap(
                    Multicolinearity_matrix, 
                    cmap=cmap, 
                    annot=True, 
                    ax=ax[2]).set(title='Condition Index', xlabel=' ', ylabel=' ')
                
            if plot != 'dash':
                fig, ax = plt.subplots(figsize=(14, 6))
                sns.heatmap(
                    Multicolinearity_matrix, 
                    cmap=cmap,
                    annot=True).set(title='Condition Index', xlabel=' ', ylabel=' ')
            
            self.multico = [feat for idx, feat in zip(CI, train.corr().iloc[1:, 1:].columns) if idx > 30]
        #-------------------------------------------VIF-------------------------------------------------
        from statsmodels.stats.outliers_influence import variance_inflation_factor
  
        # the independent variables set
        X = self.df.drop('Survived', axis=1)

        # VIF dataframe
        vif_data = pd.DataFrame()
        vif_data["feature"] = X.columns

        # calculating VIF for each feature
        VIF = {feat:variance_inflation_factor(X.dropna().values, i) for i, feat in zip(range(len(X.columns)), X.columns)}
        self.VIF = pd.DataFrame(VIF, index=['VIF']).T.sort_values('VIF', ascending=False)
        #------------------------------Pearsons_R------------------------------
        Pearsons_R = self.df.corr()
        cmatrix = abs(Pearsons_R).sort_values(by=self.target,ascending=False)
        
        #------------------------------Pearsons'R with target------------------------------
        if plot == "pearsons_target" or plot == 'dash':
            if plot == 'dash':
                sns.lineplot( 
                    x=[i + 1 for i in range(len(cmatrix[[self.target]][1:]))], 
                    y=cmatrix[self.target][1:].to_list(), 
                    linewidth=2, ax=ax[3], color='seagreen').set(title="Pearson'R with Target".title(), xlabel=' ')
                
            if plot != 'dash':
                fig, ax = plt.subplots(figsize=(14, 6))
                sns.lineplot( 
                    x=[i + 1 for i in range(len(cmatrix[[self.target]][1:]))], 
                    y=cmatrix[self.target][1:].to_list(), 
                    linewidth=2, color='seagreen').set(title="Pearson'R with Target".title(), xlabel=' ')
        
        #------------------------------Pearsons'R------------------------------
        if plot == "pearsonsr" or plot == 'dash':
            corr_mat = self.df.corr().stack().reset_index(name="correlation")
            g = sns.relplot(
                    data=corr_mat,
                    x="level_0", y="level_1", hue="correlation", size="correlation",
                    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
                    height=11, sizes=(70, 270), size_norm=(-.2, .8)
                ).set(title="Pearsons'R")

            # Tweak the figure to finalize
            g.set(xlabel="", ylabel="", aspect="equal")
            g.despine(left=True, bottom=True)
            g.ax.margins(.02)
            for label in g.ax.get_xticklabels():
                label.set_rotation(90)
            for artist in g.legend.legendHandles:
                artist.set_edgecolor(".7")

            plt.show()
            
            corr_matrix = self.df.corr()
            corr_with_tar = corr_matrix[target][1:].to_dict()
            corr_with_feat = {}
            for col in corr_matrix.columns:
                for row in corr_matrix.columns:
                    if col != row or row != col:
                        if target != col and target != row:
                            if corr_matrix[col][row] > 0.85:
                                if f'{row}-{col}' not in corr_with_feat.keys():
                                    corr_with_feat[f'{col}-{row}'] = abs(corr_matrix[col][row])

            corr_with_feat = list(corr_with_feat.keys())

            p1 = [p.split('-')[0] for idx, p in enumerate(corr_with_feat)]
            p2 = [p.split('-')[1] for idx, p in enumerate(corr_with_feat)]
            self.pearsonsr = list(set(np.where(p1 > p2, p1, p2)))
            
        self.drop = (self.multico + self.missing + self.pearsonsr).to_list()
