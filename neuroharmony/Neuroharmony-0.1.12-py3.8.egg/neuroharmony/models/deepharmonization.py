"""Neuroharmony classes and functions."""
from keras_tuner import HyperModel
from keras_tuner import RandomSearch
from numpy import unique
from pandas.core.generic import NDFrame
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import tensorflow as tf

from neuroharmony.models.harmonization import Neuroharmony, _label_encode_covariates


class Regressor(HyperModel):
    """Short summary.

    Parameters
    ----------
    normalizer : type
        Description of parameter `normalizer`.
    n_output : type
        Description of parameter `n_output`.
    units : type
        Description of parameter `units`.
    param_distributions : type
        Description of parameter `param_distributions`.

    Attributes
    ----------
    normalizer
    units
    param_distributions

    """

    def __init__(
        self,
        normalizer,
        n_output,
        units=512,
        param_distributions=dict(learning_rate=[100, 200, 500], batch_size=[256, 512], n_layers=[3, 5],),
    ):
        """Initiate class.

        Parameters
        ----------
        normalizer : keras normalizer
            Layer used to normalize the dataset.
        n_layers : int
            Maximum number of deep layers tried by the model tunner `n_layers`.

        Returns
        -------
        type
            Description of returned object.

        """
        self.normalizer = normalizer
        self.n_output = n_output
        self.units = units
        self.param_distributions = param_distributions

    def build(self, hp):
        """Buid the model using the hyperparameter search.

        Parameters
        ----------
        hp : Internal object from Keras.
            This is a required object from kerastuner to iterate values in the hyperparameter search.

        Returns
        -------
        keras model
            A deep learning model to perform regression.
        """
        hp_learning_rate = hp.Choice("learning_rate", values=self.param_distributions["learning_rate"])
        hp_n_layers = hp.Choice("n_layers", values=self.param_distributions["n_layers"])
        model = tf.keras.Sequential()
        model.add(self.normalizer)
        # for i in range(hp_n_layers):
        model.add(tf.keras.layers.Dense(self.units, activation="relu"))
        model.add(tf.keras.layers.Dense(self.n_output))
        model.compile(
            loss="mean_absolute_error", optimizer=tf.keras.optimizers.Adam(learning_rate=hp_learning_rate),
        )
        return model


class DeepNeuroharmony(Neuroharmony):
    """Harmonization tool to mitigate scanner bias.

    Parameters
    ----------
    features : list
        Target features to be harmonized, for example, ROIs.
    regression_features : list
        Features used to derive harmonization rules, for example, IQMs.
    covariates : list
        Variables for which we want to eliminate the bias, for example, age, sex, and scanner.
    estimator : sklearn estimator, default=RandomForestRegressor()
        Model to make the harmonization regression.
    scaler : sklearn scaler, default=StandardScaler()
        Scaler used as the first step of the harmonization regression.
    model_strategy : {"single", "full"}, default="single"
        If "single" one model will be trained for each single feature in `features`. If "full" it will use a single
        model to regress all the `features` at once.
    param_distributions : dict, default=dict(RandomForestRegressor__n_estimators=[100, 200, 500],
                                             RandomForestRegressor__warm_start=[False, True], )
        Distribution of parameters to be testes on the RandomizedSearchCV.
    **estimator_args : dict
        Parameters for the estimator.
    **scaler_args : dict
        Parameters for the scaler.
    **randomized_search_args : dict
        Parameters for the RandomizedSearchCV.
        See https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html
    **pipeline_args : dict
        Parameters for the sklearn Pipeline.
        See https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

    Attributes
    ----------
    X_harmonized_ : NDFrame [n_subjects, n_features]
        Input data harmonized.
    leaveonegroupout_ :
        Leave One Group Out cross-validator.
    models_by_feature_ :
        Estimators by features.
    """

    def __init__(
        self,
        features,
        regression_features,
        covariates,
        eliminate_variance,
        estimator=None,
        scaler=StandardScaler(),
        model_strategy="single",
        param_distributions=dict(learning_rate=[100, 200, 500], n_layers=[3, 5],),
        batch_size=512,
        units=256,
        epochs=100,
    ):
        """Init class."""
        super(DeepNeuroharmony, self).__init__(
            features, regression_features, covariates, eliminate_variance,
        )
        self.features = features
        self.regression_features = regression_features
        self.covariates = covariates
        self.eliminate_variance = eliminate_variance
        self.estimator = estimator
        self.scaler = scaler
        self.model_strategy = model_strategy
        self.param_distributions = param_distributions
        self.batch_size = batch_size
        self.units = units
        self.epochs = epochs

    def _get_callbacks(self):
        """Return a function used to stop fitting when over fitting starts to be evident in the loss function.

        Returns
        -------
        tuple
            Tuple with the function used internally to truncate fitting epochs.

        """
        return (tf.keras.callbacks.EarlyStopping(monitor="loss", patience=200),)

    def fit(self, df):
        self._check_data(df.copy())
        self._check_training_ranges(df.copy())
        df = self._check_index(df.copy())
        df, self.encoders = _label_encode_covariates(df.copy(), unique(self.covariates + self.eliminate_variance))
        X_train_split, y_train_split = self._run_combat(df.copy())
        X_train_split = X_train_split[self.regression_features + self.features].values.astype("float32")
        y_train_split = y_train_split[self.features].values.astype("float32")
        self.models_by_feature_ = {}

        self.n_output = y_train_split.shape[1]
        self.normalizer = tf.keras.layers.experimental.preprocessing.Normalization()
        self.normalizer.adapt(X_train_split)

        if not self.estimator:
            estimator = Regressor(normalizer=self.normalizer, n_output=self.n_output)

        self.tuner = RandomSearch(
            estimator,
            objective="loss",
            max_trials=4,
            executions_per_trial=1,
            directory="./tunning",
            project_name="DeepNeuroharmonyTunning",
            overwrite=True,
        )

        self.tuner.search(
            X_train_split, y_train_split, epochs=10, batch_size=10, validation_split=0.2, use_multiprocessing=True,
        )

        self.best_estimator_ = self.tuner.get_best_models(num_models=1)[0]
        self.hist = self.best_estimator_.fit(
            X_train_split,
            y_train_split,
            validation_split=0.2,
            verbose=0,
            epochs=self.epochs,
            callbacks=self._get_callbacks(),
        )
        return self

    def save(self, path="./"):
        """Short summary.

        Parameters
        ----------
        path : type
            Description of parameter `path`.

        Returns
        -------
        type
            Description of returned object.

        Examples
        -------
        Examples should be written in doctest format, and
        should illustrate how to use the function/class.
        >>>

        """
        # tf.keras.models.save_model(self.enc, f"{path}/enc.h5")
        # tf.keras.models.save_model(self.dec, f"{path}/dec.h5")
        # tf.keras.models.save_model(self.disc, f"{path}/disc.h5")
        # joblib.dump(self.enc_age, f"{path}enc_age.joblib")
        # joblib.dump(self.enc_gender, f"{path}/enc_gender.joblib")
        # joblib.dump(self.pre_scaler, f"{path}/pre_scaler.joblib")
        # joblib.dump(self.pre_scaler, f"{path}/pre_scaler.joblib")
        # joblib.dump(self.pos_scaler, f"{path}/pos_scaler.joblib")

        pass
