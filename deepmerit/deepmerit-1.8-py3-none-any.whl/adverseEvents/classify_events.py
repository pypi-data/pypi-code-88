# Authors : Akhil Chitreddy and Gautam Nair

import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import fbeta_score, precision_score, make_scorer, average_precision_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import auc, roc_curve, roc_auc_score

class LogReg:
    def __init__(self,X_train,X_test,y_train,y_test,mlb1,collist):
        self.X_train=X_train
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
        self.mlb1=mlb1
        self.collist=collist

    def model(self):
        clf=OneVsRestClassifier(LogisticRegression(C=20, penalty='l2'))
        clf.fit(self.X_train, self.y_train)
        score=fbeta_score(self.y_test, clf.predict(self.X_test), beta=2, average=None)
        avg_sample_score=fbeta_score(self.y_test, clf.predict(self.X_test), beta=2, average='samples')
        avg_prec=average_precision_score(self.y_test.T, clf.predict(self.X_test).T)
        metrics = [score, avg_sample_score, roc_auc_score(self.y_test.T, clf.predict_proba(self.X_test).T)]
        app = dict()
        app['Classwise Scores'] = ([(self.mlb1.classes_[l], score[l]) for l in score.argsort()[::-1]])
        app['F2 Score'] = avg_sample_score
        app['ROC_AUC'] = roc_auc_score(self.y_test.T, clf.predict_proba(self.X_test).T)
        app['Precision Score Avg (PR Curve)'] = avg_prec
        return app


class RandomFor:
    def __init__(self,X_train,X_test,y_train,y_test,mlb1,collist,df):
        self.X_train=X_train
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
        self.mlb1=mlb1
        self.collist=collist
        self.df=df
        self.clf=OneVsRestClassifier(RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42, min_samples_split=10))
        self.clf.fit(self.X_train, self.y_train)

    def model(self):
        score=fbeta_score(self.y_test, self.clf.predict(self.X_test), beta=2, average=None)
        avg_sample_score=fbeta_score(self.y_test, self.clf.predict(self.X_test), beta=2, average='samples')
        avg_prec=average_precision_score(self.y_test.T, self.clf.predict(self.X_test).T)
        metrics = [score, avg_sample_score, roc_auc_score(self.y_test.T, self.clf.predict_proba(self.X_test).T)]
        app = dict()
        app['Classwise Scores'] = ([(self.mlb1.classes_[l], score[l]) for l in score.argsort()[::-1]])
        app['F2 Score'] = avg_sample_score
        app['ROC_AUC'] = roc_auc_score(self.y_test.T, self.clf.predict_proba(self.X_test).T)
        app['Precision Score Avg (PR Curve)'] = avg_prec
        return app

    def predict(self):
        j=0
        l=[]
        for i in (self.mlb1.inverse_transform(self.clf.predict(self.df))):
            a=list(self.df.iloc[j])
            a.append(i)
            l.append(a)
            j+=1
        self.collist=self.collist.append('side_effect')
        df=pd.DataFrame(l, columns = self.collist)
        df.to_csv('test_data_output.csv',index=False)
        return "Prediction done in 'test_data_output.csv' file"


class SVC:
    def __init__(self,X_train,X_test,y_train,y_test,mlb1):
        self.X_train=X_train
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
        self.mlb1=mlb1

    def model(self):
        clf=OneVsRestClassifier(SVC(probability=True, kernel='rbf'))
        clf.fit(self.X_train, self.y_train)
        score=fbeta_score(self.y_test, clf.predict(self.X_test), beta=2, average=None)
        avg_sample_score=fbeta_score(self.y_test, clf.predict(self.X_test), beta=2, average='samples')
        avg_prec=average_precision_score(self.y_test.T, clf.predict(self.X_test).T)
        metrics = [score, avg_sample_score, roc_auc_score(self.y_test.T, clf.predict_proba(self.X_test).T)]
        app = dict()
        app['Classwise Scores'] = ([(self.mlb1.classes_[l], score[l]) for l in score.argsort()[::-1]])
        app['F2 Score'] = avg_sample_score
        app['ROC_AUC'] = roc_auc_score(self.y_test.T, clf.predict_proba(self.X_test).T)
        app['Precision Score Avg (PR Curve)'] = avg_prec
        return app


class Gauss:
    def __init__(self,X_train,X_test,y_train,y_test,mlb1):
        self.X_train=X_train
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
        self.mlb1=mlb1

    def model(self):
        clf=OneVsRestClassifier(GaussianNB())
        clf.fit(self.X_train, self.y_train)
        score=fbeta_score(self.y_test, clf.predict(self.X_test), beta=2, average=None)
        avg_sample_score=fbeta_score(self.y_test, clf.predict(self.X_test), beta=2, average='samples')
        avg_prec=average_precision_score(self.y_test.T, clf.predict(self.X_test).T)
        metrics = [score, avg_sample_score, roc_auc_score(self.y_test.T, clf.predict_proba(self.X_test).T)]
        app = dict()
        app['Classwise Scores'] = ([(self.mlb1.classes_[l], score[l]) for l in score.argsort()[::-1]])
        app['F2 Score'] = avg_sample_score
        app['ROC_AUC'] = roc_auc_score(self.y_test.T, clf.predict_proba(self.X_test).T)
        app['Precision Score Avg (PR Curve)'] = avg_prec
        return app
