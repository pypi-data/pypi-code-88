#our code here

#import required libraries

import pandas as pd  
import numpy as np
from catboost import CatBoostRegressor, CatBoostClassifier

class FeatureImportance:
    def __init__(self):
        pass
    

    def model_build(self,df,target,verbose): 
    
#     Purpose == function for identifying if it is regression or classification task and train the model accordingly
#     function parameter == dataframe and target variable 
#     body == identifying problem, train the model with data
#     return type == trained model 
    
        self.dataframe_treatment(df,target,verbose) # calling function to treat missing values and unique value columns
    
        X=df.drop([target],axis=1) # create X or indepent variable set of the dataset
        y=df[target]               # create y or target variable
    
        categorical_features_indices = np.where(X.dtypes == 'O')[0] #pickup column values for categorical variable
    
    # checking the target variable is Object or not. If it is object then we'll use classification
    # otherwise we will use regression 
    
        if df[target].dtype == 'O' or df[target].nunique()<20:                    # 'O' refers that column is object type
            if verbose==1:
                print('Classifier is Running...\n')
            classifier_model = CatBoostClassifier()    # use classifier for categorical target
            classifier_model.fit(X, y,cat_features=categorical_features_indices,silent=True) #training done 
            return classifier_model  # returns the model
    
        else:
            if verbose==1:
                print('Regression is Running...\n')
            regressor_model = CatBoostRegressor()      # regression method selected for continuous target
            regressor_model.fit(X, y,cat_features=categorical_features_indices,silent=True) #training done
            return regressor_model   # returns the model

    def get_important_feature(self,df,target,no_of_feature=None,verbose=0): ###### MAIN FUNCTION #######
    
#     Purpose == MAIN FUNCTION, Should be public, This shows important features of a model based on dataset
#     function parameter == dataframe and target variable 
#     body == shows model's feature importance
#     return type == None 
        self.df = df
        self.target = target

        model = self.model_build(df,target,verbose) # calling the function to get the ML model
        imp_feat=pd.Series(model.feature_importances_,index=df.drop([target],axis=1).columns) # getting feature's from model
        return imp_feat.sort_values(ascending=False)[:no_of_feature].to_dict() #return features

    def dataframe_treatment(self,df,target,verbose):  ####### NULL and Unique value #######

#     Purpose == Handles Nulls in dataset target, remove columns with unique value (e.g. ID)
#     function parameter == dataframe and target variable 
#     body == NULL treatment, column with unique value handles
#     return type == None 

        if df[target].isnull().sum()>0: #checks and removes any NULL values from Target
            if verbose==1:
                print('\n Deleting ',df[target].isnull().sum(),'Nos of rows for Null values in target')
            df.dropna(subset=[target],inplace=True)
        
        cat_var = [col for col in df.columns if df[col].dtype=='O' and col != target] #pick up categorical columns except target
    
        for cat_col in cat_var: #fill NULLs of categorical columns with "Missing" string
            if df[cat_col].isnull().sum()>0 and verbose==1:
                print('Replace Missing value of ',cat_col)
            df[cat_col].fillna('Missing',inplace=True)
        
        for col in df.columns:
            if (df[col].nunique()/len(df)==1):
                if verbose==1:
                    print('Deleting unique column =',col)
                df.drop([col],axis=1,inplace=True)
