# Regression Error Learning Model
class LearnRegressionError:
    """
    Create the Regression Error Learning Object

    train: <class 'pandas.core.frame.DataFrame'>
      Pass copy of Training Dataset used to train the Machine Learning model

    validation: <class 'pandas.core.frame.DataFrame'>
      Pass copy of Validation Dataset to test the Machine Learning model

    test: <class 'pandas.core.frame.DataFrame'>
      Pass copy of Testing Dataset on which predictions are to be computed.

    current_model_features_list: <class 'list'>
      List of features used to train the current model

    output_label: <class 'str'>
      Original Output Label in the dataset

    current_model: sklearn object
      The current Machine Learning Model used to generate predictions

    focus_metric: <class 'str'>
      Values can only be 'mae','rmse','rmsle' or 'r2score'.

    include_current_model_predictions: <class 'bool'>
      Pass True to include predictions from the current model in training the error learning model else False in order to not include the predictions from current model for training the error model.
    """

    # Importing important libraries
    np = __import__('numpy')
    pd = __import__('pandas')

    # Class constructor to initialise the input arguments
    def __init__(self, train, validation, test, current_model_features_list, output_label, current_model, focus_metric,
                 include_current_model_predictions=False):

        # Raise Exception if train is not a pandas DataFrame
        if str(type(train)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('train is not a pandas DataFrame type object.')
        else:
            self.train = train

        # Raise Exception if test is not a pandas DataFrame
        if str(type(validation)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('validation is not a pandas DataFrame type object.')
        else:
            self.validation = validation

        # Raise Exception if test is not a pandas DataFrame
        if str(type(test)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('test is not a pandas DataFrame type object.')
        else:
            self.test = test

        # Raise Exception if current_model_features_list is not a list type object
        if str(type(current_model_features_list)) != "<class 'list'>":
            raise Exception('current_model_features_list is not a list object.')
        else:
            self.current_model_features_list = current_model_features_list

        # Raise Exception if output_label is not a string type object
        if str(type(output_label)) != "<class 'str'>":
            raise Exception('output_label is not a str object.')
        else:
            self.output_label = output_label

        # Raise Exception if current_model is not a Machine Learning model
        if str(type(current_model)).find('sklearn') == -1:
            raise Exception('current_model is not a sklearn type object.')
        else:
            self.current_model = current_model

        # Raise Exception if focus_metric is not a string type object and does not contain specific values
        if str(type(focus_metric)) != "<class 'str'>":
            raise Exception('focus_metric is not a str object.')
        elif focus_metric not in ['mae', 'rmse', 'rmsle', 'r2score']:
            raise Exception("metric takes either 'mae' or 'rmse' or 'rmsle' or 'r2score'.")
        else:
            self.focus_metric = focus_metric

        # Raise Exception if include_current_model_predictions is not a bool type object
        if str(type(include_current_model_predictions)) != "<class 'bool'>":
            raise Exception('include_current_model_predictions is not a bool object.')
        else:
            self.include_current_model_predictions = include_current_model_predictions

        # Python list for storing the feature list of error model
        if include_current_model_predictions == True:
            self.er_model_features_list = self.current_model_features_list.copy()
            self.er_model_features_list.append('Current Model Predictions')
        else:
            self.er_model_features_list = current_model_features_list

        self.algorithm_performance_df = 0  # Pandas dataframe for storing performance of all the models on Validation and Test sets
        self.error_model = 0  # Object to store the final error model
        self.error_model_algorithm = 0  # Algorithm used for training the final error model

    # Makes prediction via the current model and keeps the error computed
    def fit_current_model(self):
        """
        This method generates predictions using the current model provided and computes the error of the same.
        """
        # Generating predictions on Train, Validation and Test
        prediction_train = self.current_model.predict(self.train[self.current_model_features_list])
        prediction_validation = self.current_model.predict(self.validation[self.current_model_features_list])
        prediction_test = self.current_model.predict(self.test[self.current_model_features_list])

        # Saving predictions in Train, Validation and Test
        self.train['Current Model Predictions'] = prediction_train
        self.validation['Current Model Predictions'] = prediction_validation
        self.test['Current Model Predictions'] = prediction_test

        # Computing error on Train, Validation and Test
        self.train['Current Model Error'] = (self.train[self.output_label] - self.train['Current Model Predictions'])
        self.validation['Current Model Error'] = (
                    self.validation[self.output_label] - self.validation['Current Model Predictions'])
        self.test['Current Model Error'] = (self.test[self.output_label] - self.test['Current Model Predictions'])

    # Updates er_model_features_list if any feature engineering is done using Current Model Predictions
    def update_er_model_features_list(self, updated_er_model_features_list):
        """
        updated_er_model_features_list: <class 'list'>
          Use this method only if you have done Feature Engineering using the predictions from Current Model. You need to update the list of features used to train the Error Learning Model
        """
        # Set the updated er_model_features_list in the er_model_features_list variable
        self.er_model_features_list = updated_er_model_features_list

    # Run different ML algorithms to see which algorithm is best for predicting error
    def er_fit_and_predict(self):
        """
        This method fits and computes the Error Learning model.
        """
        from sklearn.linear_model import LinearRegression
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.ensemble import AdaBoostRegressor
        from sklearn.svm import SVR
        from sklearn.ensemble import GradientBoostingRegressor
        from xgboost import XGBRegressor
        from lightgbm import LGBMRegressor
        from sklearn.neighbors import KNeighborsRegressor
        from sklearn.metrics import mean_absolute_error
        from sklearn.metrics import mean_squared_error
        from sklearn.metrics import mean_squared_log_error
        from sklearn.metrics import r2_score

        # Creating a dictionary of all possible algorithms
        models_list = {
            'Linear Regression': LinearRegression(),
            'Decision Tree': DecisionTreeRegressor(),
            'Random Forest': RandomForestRegressor(),
            'Ada Boost': AdaBoostRegressor(),
            'SVR': SVR(),
            'Gradient Boosting': GradientBoostingRegressor(),
            'XG Boost': XGBRegressor(),
            'Light GBM': LGBMRegressor(),
            'KNearest Neighbors': KNeighborsRegressor()
        }

        # Initialising the pandas dataframe to store metric values for different algorithms
        self.algorithm_performance_df = self.pd.DataFrame(
            columns=['Trained Model', 'Error Model Predictions Validation', 'Error Model Predictions Test',
                     'Final Output Validation', 'Final Output Test',
                     'Error Model Validation MAE', 'Error Model Validation RMSE', 'Error Model Validation RMSLE',
                     'Error Model Validation R2-Score',
                     'Error Model Test MAE', 'Error Model Test RMSE', 'Error Model Test RMSLE',
                     'Error Model Test R2-Score',
                     'Final Output Validation MAE', 'Final Output Validation RMSE', 'Final Output Validation RMSLE',
                     'Final Output Validation R2-Score',
                     'Final Output Test MAE', 'Final Output Test RMSE', 'Final Output Test RMSLE',
                     'Final Output Test R2-Score'])

        # Iterate every model and calculate predictions. Further, store model performance metrics in the assigned dataframe
        for key, model in models_list.items():

            # Fitting the error model and generating predictions
            model.fit(self.train[self.er_model_features_list], self.train['Current Model Error'])
            model_predictions_validation = model.predict(self.validation[self.er_model_features_list])
            model_predictions_test = model.predict(self.test[self.er_model_features_list])

            self.algorithm_performance_df.loc[key, 'Trained Model'] = model
            self.algorithm_performance_df.loc[key, 'Error Model Predictions Validation'] = model_predictions_validation
            self.algorithm_performance_df.loc[key, 'Error Model Predictions Test'] = model_predictions_test

            # Populating Metric Scores for Validation Error Model
            self.algorithm_performance_df.loc[key, 'Error Model Validation MAE'] = mean_absolute_error(self.validation['Current Model Error'], model_predictions_validation)
            self.algorithm_performance_df.loc[key, 'Error Model Validation RMSE'] = self.np.sqrt(mean_squared_error(self.validation['Current Model Error'],model_predictions_validation))
            if any(model_predictions_validation < 0):
                pass
            else:
                self.algorithm_performance_df.loc[key, 'Error Model Validation RMSLE'] = self.np.sqrt(mean_squared_log_error(self.validation['Current Model Error'],model_predictions_validation))
            self.algorithm_performance_df.loc[key, 'Error Model Validation R2-Score'] = r2_score(self.validation['Current Model Error'], model_predictions_validation)

            # Populating Metric Scores for Test Error Model
            self.algorithm_performance_df.loc[key, 'Error Model Test MAE'] = mean_absolute_error(
                self.test['Current Model Error'], model_predictions_test)
            self.algorithm_performance_df.loc[key, 'Error Model Test RMSE'] = self.np.sqrt(
                mean_squared_error(self.test['Current Model Error'], model_predictions_test))
            if any(model_predictions_validation < 0):
                pass
            else:
                self.algorithm_performance_df.loc[key, 'Error Model Test RMSLE'] = self.np.sqrt(
                    mean_squared_log_error(self.test['Current Model Error'],
                                                                model_predictions_test))
            self.algorithm_performance_df.loc[key, 'Error Model Test R2-Score'] = r2_score(
                self.test['Current Model Error'], model_predictions_test)

            # Populating Metric Scores for Validation Final Output
            final_output_validation = self.validation['Current Model Predictions'] + model_predictions_validation
            self.algorithm_performance_df.loc[key, 'Final Output Validation'] = final_output_validation.tolist()
            self.algorithm_performance_df.loc[
                key, 'Final Output Validation MAE'] = mean_absolute_error(
                self.validation[self.output_label], final_output_validation)
            self.algorithm_performance_df.loc[key, 'Final Output Validation RMSE'] = self.np.sqrt(
                mean_squared_error(self.validation[self.output_label], final_output_validation))
            if any(final_output_validation < 0):
                pass
            else:
                self.algorithm_performance_df.loc[key, 'Final Output Validation RMSLE'] = self.np.sqrt(
                    mean_squared_log_error(self.validation[self.output_label],
                                                                final_output_validation))
            self.algorithm_performance_df.loc[key, 'Final Output Validation R2-Score'] = r2_score(
                self.validation[self.output_label], final_output_validation)

            # Populating Metric Scores for Test Final Output
            final_output_test = self.test['Current Model Predictions'] + model_predictions_test
            self.algorithm_performance_df.loc[key, 'Final Output Test'] = final_output_test.tolist()
            self.algorithm_performance_df.loc[key, 'Final Output Test MAE'] = mean_absolute_error(
                self.test[self.output_label], final_output_test)
            self.algorithm_performance_df.loc[key, 'Final Output Test RMSE'] = self.np.sqrt(
                mean_squared_error(self.test[self.output_label], final_output_test))
            if any(final_output_test < 0):
                pass
            else:
                self.algorithm_performance_df.loc[key, 'Final Output Test RMSLE'] = self.np.sqrt(
                    mean_squared_log_error(self.test[self.output_label], final_output_test))
            self.algorithm_performance_df.loc[key, 'Final Output Test R2-Score'] = r2_score(
                self.test[self.output_label], final_output_test)

        # Sorting Dataframe as per selected evaluation metric
        if self.focus_metric == 'mae':
            self.algorithm_performance_df.sort_values(by='Final Output Validation MAE', inplace=True, ascending=True)
        elif self.focus_metric == 'rmse':
            self.algorithm_performance_df.sort_values(by='Final Output Validation RMSE', inplace=True, ascending=True)
        elif self.focus_metric == 'rmsle':
            self.algorithm_performance_df.sort_values(by='Final Output Validation RMSLE', inplace=True, ascending=True)
        else:
            self.algorithm_performance_df.sort_values(by='Final Output Validation R2-Score', inplace=True,
                                                      ascending=False)

        # Storing the best working model
        self.error_model_algorithm = self.algorithm_performance_df.index[0]
        self.error_model = self.algorithm_performance_df.loc[self.error_model_algorithm, 'Trained Model']

    # Predict via Current Model on final_prediction_set
    def predict_current_model(self, final_prediction_set):
        """
        This method generates predictions via the current model.
        """
        current_model_predictions = self.current_model.predict(final_prediction_set[self.current_model_features_list])
        final_prediction_set['Current Model Predictions'] = current_model_predictions

        return final_prediction_set

    # Predict via Error Model on final_prediction_set
    def predict_er_model(self, final_prediction_set):
        """
        This method generates predictions via the error learning model.
        """
        er_model_predictions = self.error_model.predict(final_prediction_set[self.er_model_features_list])
        final_prediction_set['Error Model Predictions'] = er_model_predictions

        return final_prediction_set

    # Calculate the final prediction
    def output_transformer(self, final_prediction_set):
        """
        This method generates the final predictions based on current model and error learning model.
        """
        final_prediction_set[self.output_label + ' Predictions'] = final_prediction_set['Current Model Predictions'] + \
                                                                   final_prediction_set['Error Model Predictions']

        return final_prediction_set


# Classification Error Learning Model
class LearnClassificationError:
    """
    Create the Regression Error Learning Object

    train: <class 'pandas.core.frame.DataFrame'>
      Pass copy of Training Dataset used to train the Machine Learning model

    validation: <class 'pandas.core.frame.DataFrame'>
      Pass copy of Validation Dataset to test the Machine Learning model

    test: <class 'pandas.core.frame.DataFrame'>
      Pass copy of Testing Dataset on which predictions are to be computed

    current_model_features_list: <class 'list'>
      List of features used to train the current model

    output_label: <class 'str'>
      Original Output Label in the dataset

    current_model: sklearn object
      The current Machine Learning Model used to generate predictions

    focus_metric: <class 'str'>
      Values can only be 'precision','recall', 'f1-score' or 'accuracy'.

    current_average: <class 'str'>
      Values can only be 'binary','macro','micro','weighted' or 'samples'.

    error_average: <class 'str'>
      Values can only be 'macro','micro','weighted' or 'samples'.

    include_current_model_predictions: <class 'bool'>
      Pass True to include predictions from the current model in training the error learning model else False in order to not include the predictions from current model for training the error model.

    include_current_model_probabilities: <class 'bool'>
      Pass True to include probabilities from the current model in training the error learning model else False in order to not include the probabilities from current model for training the error model.
    """

    # Importing important libraries
    np = __import__('numpy')
    pd = __import__('pandas')

    # Class constructor to initialise the input arguments
    def __init__(self, train, validation, test, current_model_features_list, output_label, current_model, focus_metric,
                 current_average, error_average, include_current_model_predictions=False,
                 include_current_model_probabilities=False):

        # Raise Exception if train is not a pandas DataFrame
        if str(type(train)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('train is not a pandas DataFrame type object.')
        else:
            self.train = train

        # Raise Exception if test is not a pandas DataFrame
        if str(type(validation)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('validation is not a pandas DataFrame type object.')
        else:
            self.validation = validation

        # Raise Exception if test is not a pandas DataFrame
        if str(type(test)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('test is not a pandas DataFrame type object.')
        else:
            self.test = test

        # Raise Exception if current_model_features_list is not a list type object
        if str(type(current_model_features_list)) != "<class 'list'>":
            raise Exception('current_model_features_list is not a list object.')
        else:
            self.current_model_features_list = current_model_features_list

        # Raise Exception if output_label is not a string type object
        if str(type(output_label)) != "<class 'str'>":
            raise Exception('output_label is not a str object.')
        else:
            self.output_label = output_label

        # Raise Exception if current_model is not a Machine Learning model
        if str(type(current_model)).find('sklearn') == -1:
            if str(type(current_model)) == "<class 'catboost.core.CatBoostClassifier'>":
                self.current_model = current_model
            else:
                raise Exception('current_model is not a sklearn type object.')
        else:
            self.current_model = current_model

        # Raise Exception if focus_metric is not a string type object and does not contain specific values
        if str(type(focus_metric)) != "<class 'str'>":
            raise Exception('focus_metric is not a str object.')
        elif focus_metric not in ['precision', 'recall', 'f1-score', 'accuracy']:
            raise Exception("metric takes either 'precision' or 'recall' or 'f1-score' or 'accuracy'.")
        else:
            self.focus_metric = focus_metric

        # Raise Exception if current_average is not a string type object and does not contain specific values
        if str(type(current_average)) != "<class 'str'>":
            raise Exception('current_average is not a str object.')
        elif current_average not in ['binary', 'macro', 'micro', 'weighted', 'samples']:
            raise Exception("current_average takes either 'binary' or 'macro' or 'micro' or 'weighted' or 'samples'.")
        else:
            self.current_average = current_average

        # Raise Exception if error_average is not a string type object and does not contain specific values
        if str(type(error_average)) != "<class 'str'>":
            raise Exception('error_average is not a str object.')
        elif error_average not in ['macro', 'micro', 'weighted', 'samples']:
            raise Exception("error_average takes either 'macro' or 'micro' or 'weighted' or 'samples'.")
        else:
            self.error_average = error_average

        # Raise Exception if include_current_model_predictions is not a bool type object
        if str(type(include_current_model_predictions)) != "<class 'bool'>":
            raise Exception('include_current_model_predictions is not a bool object.')
        else:
            self.include_current_model_predictions = include_current_model_predictions

        # Raise Exception if include_current_model_probabilities is not a bool type object
        if str(type(include_current_model_probabilities)) != "<class 'bool'>":
            raise Exception('include_current_model_probabilities is not a bool object.')
        else:
            self.include_current_model_probabilities = include_current_model_probabilities

        self.model_classes = self.train[self.output_label].unique()
        self.model_classes.sort()

        # Python list for storing the feature list of error model
        if include_current_model_predictions == True:
            self.er_model_features_list = self.current_model_features_list.copy()
            self.er_model_features_list.append('Current Model Predictions')
        else:
            self.er_model_features_list = current_model_features_list

        # Updating Python list for storing the feature list of error model
        if include_current_model_probabilities == True:
            for model_class in self.model_classes:
                self.er_model_features_list.append('Current Model Probabilities Class ' + str(model_class))

        self.error_matrix = self.pd.DataFrame(index=self.model_classes,
                                         columns=self.model_classes)  # Matrix based on error combination of different classes
        self.algorithm_performance_df = 0  # Pandas dataframe for storing performance of all the models on Validation and Test sets
        self.error_model = 0  # Object to store the final error model
        self.error_model_algorithm = 0  # Algorithm used for training the final error model

        # Preparing the classification error matrix
        counter = 1
        for index in self.error_matrix.index:
            for column in self.error_matrix.columns:
                if index != column:
                    self.error_matrix.loc[index, column] = counter
                    counter = counter + 1
                if index == column:
                    self.error_matrix.loc[index, column] = 0

    # Makes prediction via the current model and keeps the error computed
    def fit_current_model(self):
        """
        This method generates predictions using the model provided and computes the error of the same.
        """
        # Generating predictions on Train, Validation and Test
        prediction_train = self.current_model.predict(self.train[self.current_model_features_list])
        proba_train = self.current_model.predict_proba(self.train[self.current_model_features_list])

        prediction_validation = self.current_model.predict(self.validation[self.current_model_features_list])
        proba_validation = self.current_model.predict_proba(self.validation[self.current_model_features_list])

        prediction_test = self.current_model.predict(self.test[self.current_model_features_list])
        proba_test = self.current_model.predict_proba(self.test[self.current_model_features_list])

        # Saving predictions in Train, Validation and Test
        self.train['Current Model Predictions'] = prediction_train
        self.validation['Current Model Predictions'] = prediction_validation
        self.test['Current Model Predictions'] = prediction_test

        for model_class in self.model_classes:
            self.train['Current Model Probabilities Class ' + str(model_class)] = proba_train[:, model_class]
            self.validation['Current Model Probabilities Class ' + str(model_class)] = proba_validation[:, model_class]
            self.test['Current Model Probabilities Class ' + str(model_class)] = proba_test[:, model_class]

        for index in self.error_matrix.index:
            for column in self.error_matrix.columns:
                self.train.loc[(self.train[self.output_label] == index) & (
                            self.train['Current Model Predictions'] == column), 'Current Model Error'] = \
                self.error_matrix.loc[index, column]
                self.validation.loc[(self.validation[self.output_label] == index) & (
                            self.validation['Current Model Predictions'] == column), 'Current Model Error'] = \
                self.error_matrix.loc[index, column]
                self.test.loc[(self.test[self.output_label] == index) & (
                            self.test['Current Model Predictions'] == column), 'Current Model Error'] = \
                self.error_matrix.loc[index, column]

    # Updates er_model_features_list if any feature engineering is done using Current Model Predictions
    def update_er_model_features_list(self, updated_er_model_features_list):
        """
        updated_er_model_features_list: <class 'list'>
          Use this method only if you have done Feature Engineering using the predictions from Current Model. You need to update the list of features used to train the Error Learning Model
        """
        # Set the updated er_model_features_list in the er_model_features_list variable
        self.er_model_features_list = updated_er_model_features_list

    # Run different ML algorithms to see which algorithm is best for predicting error
    def er_fit_and_predict(self):
        """
        This method fits and evaluates the Error Learning model.
        """
        from sklearn.linear_model import LogisticRegression
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.ensemble import AdaBoostClassifier
        from sklearn.svm import SVC
        from sklearn.ensemble import GradientBoostingClassifier
        from xgboost import XGBClassifier
        from lightgbm import LGBMClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.naive_bayes import GaussianNB
        from catboost import CatBoostClassifier
        from sklearn.metrics import precision_score
        from sklearn.metrics import recall_score
        from sklearn.metrics import f1_score
        from sklearn.metrics import accuracy_score
        from sklearn.metrics import confusion_matrix
        from sklearn.metrics import classification_report
        
        # Creating a dictionary of all possible algorithms
        models_list = {
            'Logistic Regression': LogisticRegression(),
            'Decision Tree': DecisionTreeClassifier(),
            'Random Forest': RandomForestClassifier(),
            'Ada Boost': AdaBoostClassifier(),
            'SVC': SVC(probability=True),
            'Gradient Boosting': GradientBoostingClassifier(),
            'XG Boost': XGBClassifier(),
            'Light GBM': LGBMClassifier(),
            'KNearest Neighbors': KNeighborsClassifier(),
            'Gaussian Naive Bayes': GaussianNB(),
            'Cat Boost': CatBoostClassifier(silent=True)
        }

        # Initialising the pandas dataframe to store metric values for different algorithms
        self.algorithm_performance_df = self.pd.DataFrame(
            columns=['Trained Model', 'Error Model Predictions Validation', 'Error Model Probability Validation',
                     'Error Model Predictions Test', 'Error Model Probability Test',
                     'Error Model Validation Precision', 'Error Model Validation Recall',
                     'Error Model Validation F1-Score', 'Error Model Validation Accuracy',
                     'Error Model Validation Confusion Matrix', 'Error Model Validation Classification Report',
                     'Error Model Test Precision', 'Error Model Test Recall', 'Error Model Test F1-Score',
                     'Error Model Test Accuracy', 'Error Model Test Confusion Matrix',
                     'Error Model Test Classification Report',
                     'Final Output Validation Precision', 'Final Output Validation Recall',
                     'Final Output Validation F1-Score', 'Final Output Validation Accuracy',
                     'Final Output Validation Confusion Matrix', 'Final Output Validation Classification Report',
                     'Final Output Test Precision', 'Final Output Test Recall', 'Final Output Test F1-Score',
                     'Final Output Test Accuracy', 'Final Output Test Confusion Matrix',
                     'Final Output Test Classification Report'])

        # Iterate every model and calculate predictions. Further, store model performance metrics in the assigned dataframe
        for key, model in models_list.items():

            # Fitting the error model and generating predictions
            model.fit(self.train[self.er_model_features_list], self.train['Current Model Error'])
            model_predictions_validation = model.predict(self.validation[self.er_model_features_list])
            model_probabilities_validation = model.predict_proba(self.validation[self.er_model_features_list])
            model_predictions_test = model.predict(self.test[self.er_model_features_list])
            model_probabilities_test = model.predict_proba(self.test[self.er_model_features_list])

            self.algorithm_performance_df.loc[key, 'Trained Model'] = model
            self.algorithm_performance_df.loc[key, 'Error Model Predictions Validation'] = model_predictions_validation
            self.algorithm_performance_df.loc[
                key, 'Error Model Probability Validation'] = model_probabilities_validation
            self.algorithm_performance_df.loc[key, 'Error Model Predictions Test'] = model_predictions_test
            self.algorithm_performance_df.loc[key, 'Error Model Probability Test'] = model_probabilities_test

            # Populating Metric Scores for Validation Error Model
            self.algorithm_performance_df.loc[
                key, 'Error Model Validation Precision'] = precision_score(
                self.validation['Current Model Error'], model_predictions_validation, average=self.error_average)
            self.algorithm_performance_df.loc[key, 'Error Model Validation Recall'] = recall_score(
                self.validation['Current Model Error'], model_predictions_validation, average=self.error_average)
            self.algorithm_performance_df.loc[key, 'Error Model Validation F1-Score'] = f1_score(
                self.validation['Current Model Error'], model_predictions_validation, average=self.error_average)
            self.algorithm_performance_df.loc[
                key, 'Error Model Validation Accuracy'] = accuracy_score(
                self.validation['Current Model Error'], model_predictions_validation)
            self.algorithm_performance_df.loc[
                key, 'Error Model Validation Confusion Matrix'] = confusion_matrix(
                self.validation['Current Model Error'], model_predictions_validation)
            self.algorithm_performance_df.loc[
                key, 'Error Model Validation Classification Report'] = classification_report(
                self.validation['Current Model Error'], model_predictions_validation)

            # Populating Metric Scores for Test Error Model
            self.algorithm_performance_df.loc[key, 'Error Model Test Precision'] = precision_score(
                self.test['Current Model Error'], model_predictions_test, average=self.error_average)
            self.algorithm_performance_df.loc[key, 'Error Model Test Recall'] = recall_score(
                self.test['Current Model Error'], model_predictions_test, average=self.error_average)
            self.algorithm_performance_df.loc[key, 'Error Model Test F1-Score'] = f1_score(
                self.test['Current Model Error'], model_predictions_test, average=self.error_average)
            self.algorithm_performance_df.loc[key, 'Error Model Test Accuracy'] = accuracy_score(
                self.test['Current Model Error'], model_predictions_test)
            self.algorithm_performance_df.loc[
                key, 'Error Model Test Confusion Matrix'] = confusion_matrix(
                self.test['Current Model Error'], model_predictions_test)
            self.algorithm_performance_df.loc[
                key, 'Error Model Test Classification Report'] = classification_report(
                self.test['Current Model Error'], model_predictions_test)

            num_classes = len(self.model_classes)

            # Populating Metric Scores for Validation Final Output
            final_output_validation = self.pd.DataFrame(
                columns=['Current Model Predictions', 'Error Model Predictions', 'Final Output'])
            final_output_validation['Current Model Predictions'] = self.validation['Current Model Predictions']
            final_output_validation['Error Model Predictions'] = model_predictions_validation
            final_output_validation.loc[final_output_validation['Error Model Predictions'] == 0, 'Final Output'] = \
            final_output_validation.loc[
                final_output_validation['Error Model Predictions'] == 0, 'Current Model Predictions']
            for unique in final_output_validation['Error Model Predictions'].unique():
                if unique != 0:
                    column = unique / (num_classes - 1)
                    if column > int(column):
                        column = int(column)
                    else:
                        column = int(column) - 1
                    final_output_validation.loc[
                        final_output_validation['Error Model Predictions'] == unique, 'Final Output'] = column

            if self.validation[self.output_label].dtypes=='object':
                self.validation[self.output_label]=self.validation[self.output_label].astype('int64')

            final_output_validation['Final Output'] = final_output_validation['Final Output'].astype(
                str(self.validation[self.output_label].dtypes))

            self.algorithm_performance_df.loc[
                key, 'Final Output Validation Precision'] = precision_score(
                self.validation[self.output_label], final_output_validation['Final Output'],
                average=self.current_average)
            self.algorithm_performance_df.loc[
                key, 'Final Output Validation Recall'] = recall_score(
                self.validation[self.output_label], final_output_validation['Final Output'],
                average=self.current_average)
            self.algorithm_performance_df.loc[key, 'Final Output Validation F1-Score'] = f1_score(
                self.validation[self.output_label], final_output_validation['Final Output'],
                average=self.current_average)
            self.algorithm_performance_df.loc[
                key, 'Final Output Validation Accuracy'] = accuracy_score(
                self.validation[self.output_label], final_output_validation['Final Output'])
            self.algorithm_performance_df.loc[
                key, 'Final Output Validation Confusion Matrix'] = confusion_matrix(
                self.validation[self.output_label], final_output_validation['Final Output'])
            self.algorithm_performance_df.loc[
                key, 'Final Output Validation Classification Report'] = classification_report(
                self.validation[self.output_label], final_output_validation['Final Output'])

            # Populating Metric Scores for Test Final Output
            final_output_test = self.pd.DataFrame(columns=['Current Model Predictions', 'Error Model Predictions', 'Final Output'])
            final_output_test['Current Model Predictions'] = self.test['Current Model Predictions']
            final_output_test['Error Model Predictions'] = model_predictions_test
            final_output_test.loc[final_output_test['Error Model Predictions'] == 0, 'Final Output'] = \
            final_output_test.loc[final_output_test['Error Model Predictions'] == 0, 'Current Model Predictions']
            for unique in final_output_test['Error Model Predictions'].unique():
                if unique != 0:
                    column = unique / (num_classes - 1)
                    if column > int(column):
                        column = int(column)
                    else:
                        column = int(column) - 1
                    final_output_test.loc[
                        final_output_test['Error Model Predictions'] == unique, 'Final Output'] = column

            if self.test[self.output_label].dtypes == 'object':
                self.test[self.output_label] = self.test[self.output_label].astype('int64')

            final_output_test['Final Output'] = final_output_test['Final Output'].astype(
                str(self.test[self.output_label].dtypes))

            self.algorithm_performance_df.loc[
                key, 'Final Output Test Precision'] = precision_score(self.test[self.output_label],
                                                                                           final_output_test[
                                                                                               'Final Output'],
                                                                                           average=self.current_average)
            self.algorithm_performance_df.loc[key, 'Final Output Test Recall'] = recall_score(
                self.test[self.output_label], final_output_test['Final Output'], average=self.current_average)
            self.algorithm_performance_df.loc[key, 'Final Output Test F1-Score'] = f1_score(
                self.test[self.output_label], final_output_test['Final Output'], average=self.current_average)
            self.algorithm_performance_df.loc[key, 'Final Output Test Accuracy'] = accuracy_score(
                self.test[self.output_label], final_output_test['Final Output'])
            self.algorithm_performance_df.loc[
                key, 'Final Output Test Confusion Matrix'] = confusion_matrix(
                self.test[self.output_label], final_output_test['Final Output'])
            self.algorithm_performance_df.loc[
                key, 'Final Output Test Classification Report'] = classification_report(
                self.test[self.output_label], final_output_test['Final Output'])

        # Sorting Dataframe as per selected evaluation metric
        if self.focus_metric == 'precision':
            self.algorithm_performance_df.sort_values(by='Final Output Validation Precision', inplace=True,
                                                      ascending=False)
        elif self.focus_metric == 'recall':
            self.algorithm_performance_df.sort_values(by='Final Output Validation Recall', inplace=True, ascending=False)
        elif self.focus_metric == 'f1-score':
            self.algorithm_performance_df.sort_values(by='Final Output Validation F1-Score', inplace=True,
                                                      ascending=False)
        else:
            self.algorithm_performance_df.sort_values(by='Final Output Validation Accuracy', inplace=True,
                                                      ascending=False)

        # Storing the best working model
        self.error_model_algorithm = self.algorithm_performance_df.index[0]
        self.error_model = self.algorithm_performance_df.loc[self.error_model_algorithm, 'Trained Model']

    # Predict via Current Model on final_test
    def predict_current_model(self, final_prediction_set):
        """
        This method generates predictions via the current model.
        """
        current_model_predictions = self.current_model.predict(final_prediction_set[self.current_model_features_list])
        current_model_probabilities = self.current_model.predict_proba(
            final_prediction_set[self.current_model_features_list])
        final_prediction_set['Current Model Predictions'] = current_model_predictions

        for model_class in self.model_classes:
            final_prediction_set['Current Model Probabilities Class ' + str(model_class)] = current_model_probabilities[
                                                                                            :, model_class]

        return final_prediction_set

    # Predict via Error Model on final_test
    def predict_er_model(self, final_prediction_set):
        """
        This method generates predictions via the error learning model.
        """
        er_model_predictions = self.error_model.predict(final_prediction_set[self.er_model_features_list])
        final_prediction_set['Error Model Predictions'] = er_model_predictions

        return final_prediction_set

    # Calculate the final prediction
    def output_transformer(self, final_prediction_set):
        """
        This method generates the final predictions based on current model and error learning model.
        """
        num_classes = len(self.error_matrix.index)

        final_prediction_set.loc[
            final_prediction_set['Error Model Predictions'] == 0, self.output_label + ' Predictions'] = \
        final_prediction_set.loc[final_prediction_set['Error Model Predictions'] == 0, 'Current Model Predictions']
        for unique in final_prediction_set['Error Model Predictions'].unique():
            if unique != 0:
                column = unique / (num_classes - 1)
                if column > int(column):
                    column = int(column)
                else:
                    column = int(column) - 1
                final_prediction_set.loc[final_prediction_set[
                                             'Error Model Predictions'] == unique, self.output_label + ' Predictions'] = column

        final_prediction_set[self.output_label + ' Predictions'] = final_prediction_set[
            self.output_label + ' Predictions'].astype(str(self.validation[self.output_label].dtypes))

        return final_prediction_set


# Actual prediction generation
class ProductionPredictionGeneration:
    # Importing important libraries
    np = __import__('numpy')
    pd = __import__('pandas')

    # Class Constructor
    def __init__(self):
        pass

    # Predict in Prod via Current Model on final_prediction_set for Regression Use Case
    def regression_predict_current_model_prod(self, final_prediction_set, current_model_features_list, current_model):
        """
        final_prediction_set: <class 'pandas.core.frame.DataFrame'>
          Pass copy of Daily Prediction Dataset on which predictions are to be computed.
          This is the dataset without actual output label.

        current_model_features_list: <class 'list'>
          List of features used to train the current model

        current_model: sklearn object
          The current Machine Learning Model used to generate predictions
        """

        # Raise Exception if final_prediction_set is not a pandas DataFrame
        if str(type(final_prediction_set)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('final_prediction_set is not a pandas DataFrame type object.')

        # Raise Exception if current_model_features_list is not a list type object
        if str(type(current_model_features_list)) != "<class 'list'>":
            raise Exception('current_model_features_list is not a list object.')

        # Raise Exception if current_model is not a Machine Learning model
        if str(type(current_model)).find('sklearn') == -1:
            raise Exception('current_model is not a sklearn type object.')

        current_model_predictions = current_model.predict(final_prediction_set[current_model_features_list])
        final_prediction_set['Current Model Predictions'] = current_model_predictions

        return final_prediction_set

    # Predict in Prod via Error Model on final_prediction_set for Regression Use Case
    def regression_predict_error_model_prod(self, final_prediction_set, er_model_features_list, error_model,
                                            output_label):
        """
        final_prediction_set: <class 'pandas.core.frame.DataFrame'>
          Pass copy of Daily Prediction Dataset on which predictions are to be computed.
          This is the dataset without actual output label.

        er_model_features_list: <class 'list'>
          List of features used to train the error model

        error_model: sklearn object
          The Machine Learning Model used to generate error predictions

        output_label: <class 'str'>
          Original Output Label in the dataset
        """

        # Raise Exception if final_prediction_set is not a pandas DataFrame
        if str(type(final_prediction_set)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('final_prediction_set is not a pandas DataFrame type object.')

        # Raise Exception if current_model_features_list is not a list type object
        if str(type(er_model_features_list)) != "<class 'list'>":
            raise Exception('er_model_features_list is not a list object.')

        # Raise Exception if current_model is not a Machine Learning model
        if str(type(error_model)).find('sklearn') == -1:
            raise Exception('error_model is not a sklearn type object.')

        # Raise Exception if output_label is not a string type object
        if str(type(output_label)) != "<class 'str'>":
            raise Exception('output_label is not a str object.')

        error_model_predictions = error_model.predict(final_prediction_set[er_model_features_list])
        final_prediction_set['Error Model Predictions'] = error_model_predictions

        final_prediction_set[output_label + ' Predictions'] = final_prediction_set['Current Model Predictions'] + \
                                                              final_prediction_set['Error Model Predictions']

        return final_prediction_set

    # Predict in Prod via Current Model on final_prediction_set for Classification Use Case
    def classification_predict_current_model_prod(self, final_prediction_set, current_model_features_list,
                                                  model_classes, current_model):
        """
        final_prediction_set: <class 'pandas.core.frame.DataFrame'>
          Pass copy of Daily Prediction Dataset on which predictions are to be computed.
          This is the dataset without actual output label.

        current_model_features_list: <class 'list'>
          List of features used to train the current model

        model_classes: <class 'numpy.ndarray'>
          List of classes in the dataset

        current_model: sklearn object
          The current Machine Learning Model used to generate predictions
        """

        # Raise Exception if final_prediction_set is not a pandas DataFrame
        if str(type(final_prediction_set)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('final_prediction_set is not a pandas DataFrame type object.')

        # Raise Exception if current_model_features_list is not a list type object
        if str(type(current_model_features_list)) != "<class 'list'>":
            raise Exception('current_model_features_list is not a list object.')

        # Raise Exception if model_classes is not a list type object
        if str(type(model_classes)) != "<class 'numpy.ndarray'>":
            raise Exception('model_classes is not a numpy array object.')

        # Raise Exception if current_model is not a Machine Learning model
        if str(type(current_model)).find('sklearn') == -1:
            if str(type(current_model)) == "<class 'catboost.core.CatBoostClassifier'>":
                pass
            else:
                raise Exception('current_model is not a sklearn type object.')

        current_model_predictions = current_model.predict(final_prediction_set[current_model_features_list])
        current_model_probabilities = current_model.predict_proba(final_prediction_set[current_model_features_list])
        final_prediction_set['Current Model Predictions'] = current_model_predictions

        for model_class in model_classes:
            final_prediction_set['Current Model Probabilities Class ' + str(model_class)] = current_model_probabilities[
                                                                                            :, model_class]

        return final_prediction_set

    # Predict in Prod via Error Model on final_prediction_set for Classification Use Case
    def classification_predict_error_model_prod(self, final_prediction_set, er_model_features_list, error_matrix,
                                                error_model, output_label, data_type):
        """
        final_prediction_set: <class 'pandas.core.frame.DataFrame'>
          Pass copy of Daily Prediction Dataset on which predictions are to be computed.
          This is the dataset without actual output label.

        er_model_features_list: <class 'list'>
          List of features used to train the error model

        error_matrix: <class 'pandas.core.frame.DataFrame'>
          Dataframe consisting of error prediction mapping

        error_model: sklearn object
          The Machine Learning Model used to generate error predictions

        output_label: <class 'str'>
          Original Output Label in the dataset

        data_type: <class 'str'>
          Data Type of the Output Label
        """

        # Raise Exception if final_prediction_set is not a pandas DataFrame
        if str(type(final_prediction_set)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('final_prediction_set is not a pandas DataFrame type object.')

        # Raise Exception if current_model_features_list is not a list type object
        if str(type(er_model_features_list)) != "<class 'list'>":
            raise Exception('er_model_features_list is not a list object.')

        # Raise Exception if error_matrix is not a list type object
        if str(type(error_matrix)) != "<class 'pandas.core.frame.DataFrame'>":
            raise Exception('error_matrix is not a pandas DataFrame type object.')

        # Raise Exception if error_model is not a Machine Learning model
        if str(type(error_model)).find('sklearn') == -1:
            if str(type(error_model)) == "<class 'catboost.core.CatBoostClassifier'>":
                pass
            else:
                raise Exception('error_model is not a sklearn type object.')

        # Raise Exception if output_label is not a string type object
        if str(type(output_label)) != "<class 'str'>":
            raise Exception('output_label is not a str object.')

        # Raise Exception if data_type is not a string type object
        if str(type(data_type)) != "<class 'str'>":
            raise Exception('data_type is not a str object.')

        error_model_predictions = error_model.predict(final_prediction_set[er_model_features_list])
        final_prediction_set['Error Model Predictions'] = error_model_predictions

        num_classes = len(error_matrix.index)

        final_prediction_set.loc[final_prediction_set['Error Model Predictions'] == 0, output_label + ' Predictions'] = \
        final_prediction_set.loc[final_prediction_set['Error Model Predictions'] == 0, 'Current Model Predictions']
        for unique in final_prediction_set['Error Model Predictions'].unique():
            if unique != 0:
                column = unique / (num_classes - 1)
                if column > int(column):
                    column = int(column)
                else:
                    column = int(column) - 1
                final_prediction_set.loc[final_prediction_set[
                                             'Error Model Predictions'] == unique, output_label + ' Predictions'] = column

        final_prediction_set[output_label + ' Predictions'] = final_prediction_set[
            output_label + ' Predictions'].astype(data_type)

        return final_prediction_set