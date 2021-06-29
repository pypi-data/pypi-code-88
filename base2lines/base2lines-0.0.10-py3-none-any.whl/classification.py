class Classification():
    def __init__(self) -> None:
        pass
    def binaryClassification(self,dataset):
        from sklearn.impute import SimpleImputer
        import numpy as np
        import pandas as pd

        dataset = pd.DataFrame(data=dataset)
       

        #Filling the missing values
        for column in dataset.columns:
            if dataset.dtypes[column] == np.int64 or dataset.dtypes[column] == np.float64:
                imputer = SimpleImputer(missing_values = np.nan, strategy ='mean')
                test2D = dataset[column].values.reshape(1,-1)
                imputer = imputer.fit(test2D)
                dataset[column] = imputer.transform(test2D)[0] 
            else:
                imputer = SimpleImputer(missing_values= np.nan , strategy="most_frequent")
                test2D = dataset[column].values.reshape(1,-1)
                imputer = imputer.fit(test2D)
                dataset[column] = imputer.transform(test2D)[0]

        
        X = dataset.iloc[:,:-1].values
        y = dataset.iloc[:,-1].values
        #Encoding texts
        from sklearn.preprocessing import OneHotEncoder
        from sklearn.compose import ColumnTransformer
        
  
        #X = np.array(columnTransformer.fit_transform(X), dtype = np.str)
        for column in dataset.columns:
            if dataset.dtypes[column] == np.str:
              columnTransformer = ColumnTransformer([('encoder',
                                        OneHotEncoder(),
                                        [0])],
                                      remainder='passthrough')
              data = np.array(columnTransformer.fit_transform(dataset[column]),dtype = np.str)
              dataset.pop(column)
              for col in data:
                dataset[col]=data[col] 
  
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
        y_pred = rfc.predict(X_test)

        rfc_score = f1_score(y_test,y_pred,average="weighted")
        benchmark['rfc'] = rfc_score
        return benchmark




        