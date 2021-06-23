class Tourn:
    """Model Tournament Class
    ---------
    attributes:
        X_data:          training data (dependant variables)
        y_data:          training data (independent variable)
        _task :          type of task ['classification', 'regression']
        _estim:          list of all possible algorithms for the _task
        _scorer:         list of name and scorer method to calculate the model performance
        _sel_estim:      list of selected algorithms for the _task
        prel_report:     sorted DataFrame with the algorithms and metrics
        best_estimators: Dataframe with the best estimators parameters
    ---------
    methods:
        __init__:            constructor get all the estimators for a task (classification or regressor)
        pick_scorer:         allows to pick one Scorer for classification or regression tasks
        pick_estim:          defines the estimators to try
        run_prel_tournament: run a preliminary tournament with the selected algorithms (default parameters)
        gen_search_files:    method to generate hyperparameter search jsons
        run_tournament:      run the hyperparameter search using GridSearchCV or RandomizedSearchCV.
    """

    import pandas as pd
    import numpy as np
    import json
    import os

    def __init__(self, task_type, X_data, y_data):
        """Constructor Method:
        -----------
        parameters:
            task_type - (str)       - define the type of the task: ['classification','regression]
            X_data    - (DataFrame) - training data (dependant variables)
            y_data    - (DataFrame) - training data (independent variable)
        """

        from sklearn.utils import all_estimators
        from sklearn.base import ClassifierMixin, RegressorMixin
        from xgboost import XGBClassifier, XGBRegressor
        from catboost import CatBoostClassifier, CatBoostRegressor
        from lightgbm import LGBMClassifier, LGBMRegressor

        self.X_data = X_data
        self.y_data = y_data

        if task_type:
            assert task_type in [
                "classification",
                "regression",
            ], "Task must be classification or regression"
            self._task = task_type
        else:
            print("classification or regression?")
            self._task = input(
                "Define the type of task: classification or regression: "
            )
            assert self._task in [
                "classification",
                "regression",
            ], "Task must be classification or regression"

        if self._task == "classification":
            self._estim = [
                est for est in all_estimators() if issubclass(est[1], ClassifierMixin)
            ]
            self._estim.extend(
                [
                    ("XGBClassifier", XGBClassifier),
                    ("CatBoostClassifier", CatBoostClassifier),
                    ("LGBMClassifier", LGBMClassifier),
                ]
            )

        else:
            self._estim = [
                est for est in all_estimators() if issubclass(est[1], RegressorMixin)
            ]
            self._estim.extend(
                [
                    ("XGBRegressor", XGBRegressor),
                    ("CatBoostRegressor", CatBoostRegressor),
                    ("LGBMRegressor", LGBMRegressor),
                ]
            )

    def pick_scorer(self):
        """Pick Scorer:
        Allows to Pick one Scorer for classification or regression tasks
        """
        from sklearn.metrics import (
            accuracy_score,
            average_precision_score,
            f1_score,
            roc_auc_score,
            mean_absolute_error,
            mean_squared_error,
            r2_score,
        )

        clf = {
            "accuracy": accuracy_score,
            "average_precision": average_precision_score,
            "f1": f1_score,
            "roc_auc": roc_auc_score,
        }

        reg = {
            "neg_mean_absolute_error": mean_absolute_error,
            "neg_mean_squared_error": mean_squared_error,
            "r2": r2_score,
        }

        txt = ""
        i = 0
        if self._task == "classification":
            for name in clf.keys():
                txt += f"{name} : {i} \n"
                i += 1
        else:
            for name in reg.keys():
                txt += f"{name} : {i} \n"
                i += 1

        print(f"Choose one Scorer: \n\n{txt}")
        num = int(input(f"Choose number: "))

        if self._task == "classification":
            self._scorer = (
                list(clf.keys())[num],
                clf[list(clf.keys())[num]],
            )  # Name and Scorer
        elif self._task == "regression":
            self._scorer = (
                list(reg.keys())[num],
                reg[list(reg.keys())[num]],
            )  # Name and Scorer

    def pick_estim(self):
        """Defines the estimators to try"""
        txt = ""
        i = 0
        for estim, cls in self._estim:
            txt += f"{estim}: {i} \n"
            i += 1
        print(f"Select the algorithms (Comma separated): \n \n{txt}\nAll: {i}")
        inp = input(f"Select the algorithms (Comma separated): ").split(",")

        if inp[0].strip() == str(i):
            self._sel_estim = self._estim
        else:
            self._sel_estim = []
            for j in range(len(self._estim)):
                if str(j).strip() in inp:
                    self._sel_estim.append(self._estim[j])

    def _ts_split(self, X_data, y_data, train_samp):
        # TODO: doc
        X_data_look = X_data.reset_index()
        assert "timestamp" in X_data_look.columns, f"timestamp not in columns"

        total_regs = len(X_data_look.index)
        index_to_look = self.np.floor(total_regs * train_samp)
        date = X_data_look["timestamp"][index_to_look]

        X_tr = X_data.loc[X_data.index < date]
        y_tr = y_data.loc[y_data.index < date]
        X_ts = X_data.loc[X_data.index >= date]
        y_ts = y_data.loc[y_data.index >= date]

        return X_tr, X_ts, y_tr, y_ts

    def run_prel_tournament(self, train_samp=0.7, mode=None):
        """Run a preliminary tournament with the selected algorithms (default parameters)
        ----------
        parameters:
            train_samp: train sample
        ----------
        returns:
            prel_report: sorted DataFrame with the algorithms and metrics
        """

        if not hasattr(self, "_scorer"):
            self.pick_scorer()

        from sklearn.model_selection import train_test_split

        if not mode:
            X_tr, X_ts, y_tr, y_ts = train_test_split(
                self.X_data, self.y_data, train_size=train_samp, random_state=69420
            )
        elif mode == "ts":
            X_tr, X_ts, y_tr, y_ts = self._ts_split(
                self.X_data, self.y_data, train_samp=train_samp
            )
        else:
            raise ValueError(f"mode: {mode} not available")

        mod = []

        for name, estim in self._sel_estim:

            try:
                if "CatBoost" in name:
                    fitted = estim(verbose=False).fit(X=X_tr, y=y_tr)
                else:
                    fitted = estim().fit(X=X_tr, y=y_tr)

                pred_tr = fitted.predict(X_tr)
                pred_ts = fitted.predict(X_ts)
                tr_score = self._scorer[1](y_tr, pred_tr)
                ts_score = self._scorer[1](y_ts, pred_ts)
                mod.append((name, tr_score, ts_score))
            except:
                print(f"error in {name}")

        self.prel_report = self.pd.DataFrame(
            mod,
            columns=[
                "estim_name",
                f"tr_{self._scorer[0]}_score",
                f"ts_{self._scorer[0]}_score",
            ],
        )

        return self.prel_report.sort_values(
            by=self.prel_report.columns[2], ascending=False
        )

    def gen_search_files(self, path=r"hp_search/grids/"):
        """method to generate hyperparameter search jsons"""

        if not self.os.path.exists(path):
            self.os.makedirs(path)
        else:
            print("Do you want to overwrite the jsons folder?: ")
            inp = input("Y/N")

            if inp.lower() == "y":
                self.os.system(f"rm -rf {path}")
                self.os.makedirs(path)

        self._hp_path = path

        for name, estim in self._sel_estim:

            with open(rf"{path}{name}.json", "w") as file:
                if "CatBoost" not in name:
                    params = self.json.dumps(estim().get_params())
                else:
                    params = self.json.dumps(
                        {
                            "iterations": 1000,
                            "depth": 6,
                            "learning_rate": 0.03,
                            "random_seed": 0,
                            "l2_leaf_reg": 3.0,
                            "bagging_temperature": 1,
                            "verbose": False,
                        }
                    )

                dump = (
                    params.replace("{", "{\n\t")
                    .replace(", ", ",\n\t")
                    .replace("}", "]\n}")
                )
                dump = dump.replace(": ", ": [").replace(",", "],")
                file.write(dump)

        print(f"\nsearch files are in: {self._hp_path}")

    def run_tournament(
        self,
        report_path=None,
        hp_path=None,
        method="grid",
        folds=3,
        n_iter=None,
        n_jobs=-1,
        train_samp=0.7,
        mode=None,
    ):
        """run tournament:
        Run the hyperparameter search using GridSearchCV or RandomizedSearchCV.
        -----------
        parameters:
            report_path - (str)  - where to save the hp-search reports
            hp_path     - (str)  - where to load the hp-search jsons
            method      - (str)  - define the type of search ['grid', 'random']
            folds       - (int)  - define the number of cv folds
            n_jobs      - (int)  - define the number of jobs
        -----------
        returns:
            best_estimators - (DataFrame) - Sorted Dataframe with the best estimators parameters
        """

        from sklearn.model_selection import (
            GridSearchCV,
            RandomizedSearchCV,
            train_test_split,
        )
        from sklearn.metrics import make_scorer

        assert method in ["grid", "random"], f"method must be grid or random"

        if (method == "random") & (not n_iter):
            print("Specify number of iters:")
            n_iter = input("").strip()

        # Pick scorer if not done
        if not hasattr(self, "_scorer"):
            self.pick_scorer()

        # Defining the jsons path:
        if not hasattr(self, "_hp_path") and not hp_path:
            print("Specify a folder with the json files: ")
            path = input("").strip()

            for file in self.os.listdir(path):
                assert "json" in file, "folder must contain only json files"

            self._hp_path = path

        elif hp_path:
            self._hp_path = hp_path

        # Defining report path
        if not report_path:
            print("Specify a folder to save the cv reports: \n")
            report_path = input("").strip()

        if not self.os.path.exists(report_path):
            self.os.makedirs(report_path)
        else:
            print("Do you want to overwrite the reports folder?: \n")
            inp = input("Y/N")

            if inp.lower() == "y":
                self.os.system(f"rm -rf {report_path}")
                self.os.makedirs(report_path)

        # Loading jsons and searching hps:
        self._sel_estim = []

        files = self.os.listdir(self._hp_path)
        names = [file.replace(".json", "") for file in files]

        ## Defining the estimators from files
        for estim in self._estim:
            if estim[0] in names:
                self._sel_estim.append(estim)

        ## loading jsons
        hp_grids = {}
        for file, name in zip(files, names):
            f = open(f"{self._hp_path}{file}")
            hp_grids[name] = self.json.load(f)

        estims = {}
        best_estimators = []

        scorer = self._scorer[0]

        if scorer == "mape":
            scorer = make_scorer(self._scorer[1], greater_is_better=False)

        for name, estim in self._sel_estim:

            # Hyperparameter search
            print(f"\nsearching for: {name}\n")
            if method == "grid":
                estims[name] = GridSearchCV(
                    estimator=estim(),
                    param_grid=hp_grids[name],
                    scoring=scorer,
                    n_jobs=n_jobs,
                    cv=folds,
                    verbose=1,
                ).fit(self.X_data, self.y_data)
            else:
                estims[name] = RandomizedSearchCV(
                    estimator=estim(),
                    param_distributions=hp_grids[name],
                    n_iter=n_iter,
                    scoring=scorer,
                    n_jobs=n_jobs,
                    cv=folds,
                    verbose=1,
                    random_state=69420,
                ).fit(self.X_data, self.y_data)

            # Saving Report
            self.pd.DataFrame(estims[name].cv_results_).to_csv(
                f"{report_path}{name}.csv"
            )

            # Saving Best Estimators
            best_estimators.append(
                (name, estims[name].best_params_, estims[name].best_score_)
            )

        # Best Estimators
        col_names = ["name", "best_params", "best_mean_score"]
        self.best_estimators = self.pd.DataFrame(best_estimators, columns=col_names)

        # Checking overfitting
        if not mode:
            X_tr, X_ts, y_tr, y_ts = train_test_split(
                self.X_data, self.y_data, train_size=train_samp, random_state=69420
            )
        elif mode == "ts":
            X_tr, X_ts, y_tr, y_ts = self._ts_split(
                self.X_data, self.y_data, train_samp=train_samp
            )
        else:
            raise ValueError(f"mode: {mode} not available")

        mod = []
        col_names = ["name", "best_params", "tr_score", "ts_score"]
        for name, estim in self._sel_estim:
            fitted = estim(**estims[name].best_params_).fit(X_tr, y_tr)
            pred_tr = fitted.predict(X_tr)
            pred_ts = fitted.predict(X_ts)
            tr_score = self._scorer[1](y_tr, pred_tr)
            ts_score = self._scorer[1](y_ts, pred_ts)
            mod.append((name, estims[name].best_params_, tr_score, ts_score))

        self.best_estimator_scores = self.pd.DataFrame(mod, columns=col_names)
        self.best_estimator_scores.to_csv(f"{report_path}report.csv")

        return self.best_estimator_scores.sort_values("ts_score", ascending=False)
