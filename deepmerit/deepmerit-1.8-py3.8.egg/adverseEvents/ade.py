# Authors : Akhil Chitreddy and Gautam Nair

from extract_data import extract
from classify_events import LogReg,RandomFor,SVC,Gauss
import pandas as pd



class execute:
    def __init__(self,path):
        self.path=path
        self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1,self.collist,self.df=extract(self.path).preprocess()

    def Logistic(self):
        print(LogReg(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1,self.collist).model())

    def random_forest_model(self):
        print(RandomFor(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1,self.collist,self.df).model())

    def random_forest_predict(self):
        print(RandomFor(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1,self.collist,self.df).predict())

    def SVM(self):
        print(SVC(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1,self.collist).model())

    def Gaussian(self):
        print(Gauss(self.X_train1, self.X_test1, self.y_train1, self.y_test1,self.mlb1,self.collist).model())

    def feature_score(self):
        print(extract(self.path).feature_imp())
