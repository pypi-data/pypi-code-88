# Authors : Akhil Chitreddy and Gautam Nair

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

class extract:
    def __init__(self,path):
        self.path=path
        self.df=pd.read_csv(self.path)
        self.collist=list(self.df.columns)
        self.df1=pd.read_csv('github_complete_data.csv')
        #X=df.drop(columns=['side_effect'],axis=1)
        #collist=list(df.columns)
        self.X=self.df1[self.collist]
        self.Y=self.df1['side_effect']
        self.Y=self.Y.apply(lambda x: x.strip('[]').replace("'","").split(', '))
        #print(Y)
        self.X.fillna(self.X.mean(), inplace=True)
        self.mlb = MultiLabelBinarizer()
        self.y=self.mlb.fit_transform(self.Y)

    def preprocess(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.20, random_state=0)
        return X_train, X_test, y_train, y_test,self.mlb,self.collist,self.df

    def feature_imp(self):
        bestfeatures = SelectKBest(score_func=chi2, k=len(self.collist))
        fit = bestfeatures.fit(self.df,self.y)
        dfscores = pd.DataFrame(fit.scores_)
        dfcolumns = pd.DataFrame(self.df.columns)
        #concat two dataframes for better visualization
        featureScores = pd.concat([dfcolumns,dfscores],axis=1)
        featureScores.columns = ['Specs','Score']
        return featureScores
