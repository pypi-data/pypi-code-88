class Selector:
    """Selector Class
    ---------
    attributes:
        X_data    :  training data (dependant variables)
        y_data    :  training data (independent variable)
        _task     :  type of task ['classification', 'regression']
        imps      :  permutation importances DataFrame
        ivs       :  information values DataFrame
        corr      :  target correlation DataFrame
        rank      :  total ranking DataFrame
        all_corrs :  total correlation DataFrame
        excluded  :  excluded variables List
        selected  :  selected variables List
        sel_corrs :  selected correlations DataFrame
        sel_rank  :  ranks of selected variables DataFrame
    ---------
    methods:
        __init__:          constructor, creates _task and noise variables
        _weak_ens:         calculate the permutation importance on a weak ensemble
        _sub_woe_iv:       calculate woe and iv just for one variable
        _total_iv:         calculate iv for all the X_data variables
        _tar_corr:         calculate the target correlation of all variables
        ranking:           calculate variable rankings
        corr_priorization: calculates the pairwise correlation and prioritise the higher ranking on correlated ones
    ---------
    TODO:
        1. weak ensemble importance  [ok]
        2. iv or target correlation  [ok] [ok]
        3. random noise?             [ok]
        4. voting and ranking        [ok]
        5. correlation priorization  [ok]
        6. doc                       [ok]
        7. test                      [ok]
        8. H2O.ia DataRobot Bayes    [TODO]
        9. Connect performance ai    [TODO] Juan Carlos Calvo
    """

    import pandas as pd
    import numpy as np
    from scipy.stats import spearmanr

    def __init__(self, X_data, y_data, task_type=None, noise=0):
        """Constructor Method
        -----------
        parameters:
            X_data    - (DataFrame) - training data (dependant variables)
            y_data    - (DataFrame) - training data (independent variable)
            task_type - (str)       - define the type of the task: ['classification','regression]
            noise     - (int)       - define if creating noise variables
        """
        self.X_data = X_data
        self.y_data = y_data

        if noise != 0:
            self.X_data["noise_norm"] = self.np.random.normal(
                0, 1, size=self.X_data.shape[0]
            )
            self.X_data["noise_rand"] = self.np.random.uniform(
                0, 1, size=self.X_data.shape[0]
            )

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

    def _weak_ens(self, m_dep=5, n_est=20, n_rep=10):
        """calculate the permutation importance on a weak ensemble
        ----------
        parameters:
            m_dep: max depth of the weak ensemble (recommended: between 3 and 5)
            n_est: number of estimators of the weak ensemble (recommended: no more than 50)
            n_rep: number of repeats for the permutation_importance
        ----------
        returns:
            self.imps: sorted DataFrame with feature importances
        """
        from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
        from sklearn.inspection import permutation_importance

        X_data_imp = self.X_data.fillna(-999)
        y_data_imp = self.y_data.fillna(-999)

        if self._task == "classification":
            fitted = RandomForestClassifier(
                max_depth=m_dep, n_estimators=n_est, random_state=69420
            ).fit(X_data_imp, y_data_imp)
        else:
            fitted = RandomForestRegressor(
                max_depth=m_dep, n_estimators=n_est, random_state=69420
            ).fit(X_data_imp, y_data_imp)

        p_imp = permutation_importance(
            fitted, X_data_imp, y_data_imp, n_repeats=n_rep, random_state=69420
        ).importances_mean

        self.imps = self.pd.DataFrame(
            zip(X_data_imp.columns, p_imp), columns=["feature", "perm_imp"]
        ).sort_values("perm_imp", ascending=False)

        return self.imps

    def _sub_woe_iv(self, feature, good=0, bins=5):
        """calculate woe and iv just for one variable
        adapted from: https://towardsdatascience.com/attribute-relevance-analysis-in-python-iv-and-woe-b5651443fc04
        ----------
        parameters:
            feature: (string) Feature to estimate the IVs
            good:    define if good is 0 or 1 in the response variable
            bins:    number of bins to cut the feature
        ----------
        returns:
            dset:    sorted DataFrame with Weight of Evidence of every bin
            iv:      int with the Information Value
        """

        if good == 0:
            y_data = self.y_data
        else:
            y_data = -(self.y_data - 1)

        target = self.y_data.columns[0]

        binned = self.pd.DataFrame()
        binned[feature] = self.pd.qcut(self.X_data[feature], bins, duplicates="drop")

        df = self.pd.concat([binned, y_data], axis=1)

        lst = []
        for i in range(df[feature].nunique()):
            val = list(df[feature].unique())[i]
            lst.append(
                {
                    "Value": val,
                    "All": df[df[feature] == val].count()[feature],
                    "Good": df[(df[feature] == val) & (df[target] == 0)].count()[
                        feature
                    ],
                    "Bad": df[(df[feature] == val) & (df[target] == 1)].count()[
                        feature
                    ],
                }
            )

        dset = self.pd.DataFrame(lst)
        dset["Distr_Good"] = dset["Good"] / dset["Good"].sum()
        dset["Distr_Bad"] = dset["Bad"] / dset["Bad"].sum()
        dset["WoE"] = self.np.log(dset["Distr_Good"] / dset["Distr_Bad"])
        dset = dset.replace({"WoE": {self.np.inf: 0, -self.np.inf: 0}})
        dset["IV"] = (dset["Distr_Good"] - dset["Distr_Bad"]) * dset["WoE"]
        iv = dset["IV"].sum()

        dset = dset.sort_values(by="WoE")

        return dset, iv

    def _total_iv(self, good=0):
        """calculate iv for all the X_data variables
        ----------
        parameters:
            good:     define if good is 0 or 1 in the response variable
        ----------
        returns:
            self.ivs: sorted DataFrame with the Information Value of all columns
        """
        lst = []
        for feature in self.X_data.columns:
            _, iv = self._sub_woe_iv(feature, good)
            lst.append((feature, iv))

        self.ivs = self.pd.DataFrame(lst, columns=["feature", "iv"]).sort_values(
            "iv", ascending=False
        )

        return self.ivs

    def _tar_corr(self):
        """calculate the target correlation
        ----------
        returns:
            self.ivs: sorted DataFrame with the Target Correlation of all columns
        """
        from scipy.stats import spearmanr

        corr = []
        for col in self.X_data.columns:
            a = self.X_data[col].to_numpy()
            b = self.y_data.to_numpy()
            spe = abs(spearmanr(a=a, b=b, nan_policy="omit")[0])
            corr.append((col, spe))

        self.corr = self.pd.DataFrame(
            corr, columns=["feature", "target_sp_correlation"]
        ).sort_values("target_sp_correlation", ascending=False)

        return self.corr

    def ranking(self):
        """calculate variable rankings
        ----------
        returns:
            self.ivs: sorted DataFrame with the ranking of all columns
        """

        cr1 = self._weak_ens()

        if self._task == "classification":
            cr2 = self._total_iv()
        else:
            cr2 = self._tar_corr()

        # joining
        rank = cr1.merge(cr2, on="feature")

        # creating rankings
        for col in rank.columns:

            if col == "feature":
                continue
            rank[f"rank_{col}"] = rank[col].rank(method="max", ascending=False)

        # multiplying

        mult = self.pd.Series(self.np.ones(rank.shape[0]))

        for col in rank.columns:

            if not "rank" in col:
                continue

            mult *= rank[col]

        rank["mult"] = mult

        rank["rank_mult"] = mult.rank(method="max")

        self.rank = rank

        return rank

    def corr_priorization(self, th=0.1, corr_th=0.7):
        """calculates the pairwise correlation and prioritise the higher ranking on correlated ones
        ----------
        parameters:
            iv_th:   threshold of information value (the algorithm doesn't take in count
                     features with iv < iv_th)
            corr_th: threshold of correlations (if a pair of variables is highly correlated
                     corr >= corr_th, the one with less ranking is dropped)
        ----------
        returns:
            self.ivs: sorted DataFrame with the Information Value of all columns
        """
        from scipy.stats import spearmanr

        if not hasattr(self, "rank"):
            self.ranking()

        if self._task == "classification":
            rank = self.rank[self.rank["iv"] >= th].sort_values("rank_mult")
        else:
            rank = self.rank[self.rank["target_sp_correlation"] >= th].sort_values(
                "rank_mult"
            )

        vars = list(rank["feature"])

        corr = []
        for i in range(len(vars)):
            for j in range(len(vars)):

                # iterating below the diagonal
                if i < j:
                    continue

                var1 = vars[i]
                var2 = vars[j]

                # creating an auxilary dataframe and dropping nans
                df = self.X_data[[var1, var2]]

                df = df.dropna()

                # calculating correlation
                if var1 == var2:
                    sp = 1
                else:
                    sp = spearmanr(df[var1], df[var2], nan_policy="omit")[0]

                # excluding variables
                if abs(sp) >= corr_th and var1 != var2:
                    excl = var1
                else:
                    excl = None

                if var1 != var2:
                    corr.append((var1, var2, sp, excl))
                    corr.append((var2, var1, sp, excl))
                else:
                    corr.append((var1, var2, sp, excl))

        # all correlations
        self.all_corrs = self.pd.DataFrame(
            corr, columns=["var1", "var2", "spearman", "excluded"]
        )
        # excluded variables
        self.excluded = list(self.all_corrs["excluded"].drop_duplicates())
        # selected variables
        self.selected = list(rank[~rank["feature"].isin(self.excluded)]["feature"])
        # selected correlations
        self.sel_corrs = self.all_corrs[~self.all_corrs["var1"].isin(self.excluded)][
            ~self.all_corrs["var2"].isin(self.excluded)
        ]
        # filter rank, sel_rank
        self.sel_rank = self.rank[self.rank["feature"].isin(self.selected)]
