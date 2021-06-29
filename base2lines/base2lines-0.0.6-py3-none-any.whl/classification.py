class Classification():
    def __init__(self) -> None:
        pass
    def binaryClassification(self,dataset):
        from sklearn.impute import SimpleImputer
        import numpy as np
        import pandas as pd

        dataset = pd.DataFrame(data=dataset)
        #Filling the missing values
        imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
        imputer = imputer.fit(dataset)
        dataset = imputer.transform(dataset)
        X = dataset.iloc[:-1].values
        y = dataset.iloc[-1].values
        #Encoding texts
        from sklearn.preprocessing import OneHotEncoder
        from sklearn.compose import ColumnTransformer
        columnTransformer = ColumnTransformer([('encoder',
                                        OneHotEncoder(),
                                        [0])],
                                      remainder='passthrough')
  
        dataset = np.array(columnTransformer.fit_transform(dataset), dtype = np.str)   
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        y = le.fit_transform(y)
        #scaling parameters
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        X = scaler.fit_transform(X) 
        # test train split

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        #Start testing various algorithms
        from sklearn.svm import SVC
        svc = SVC(kernel='linear')
        svc.fit(X_train,y_train)
        y_pred = svc.predict(X_test)
        
        from sklearn.metrics import f1_score
        svc_score = f1_score(y_test, y_pred, average="weighted")
        # benchmark 
        benchmark = {"svc":svc_score} 

        from sklearn.ensemble import RandomForestClassifier
        rfc = RandomForestClassifier()
        rfc.fit(X_train,y_train)
        y_pred = rfc.predict(X_train)

        rfc_score = f1_score(y_test,y_pred,average="weighted")
        benchmark['rfc'] = rfc_score
        return benchmark




        pass