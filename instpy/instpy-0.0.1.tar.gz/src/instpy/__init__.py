# Multiple test libraries ----
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.multicomp import (pairwise_tukeyhsd, MultiComparison)
# -----------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Plotly  libraries ----
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
import plotly.io as pio
from plotly.subplots import make_subplots
# -----------------------------------------
# Statistics libraries ----
from statsmodels.graphics.gofplots import qqplot
from statsmodels.stats.anova import AnovaRM
from scipy import stats
from scipy.stats import (f_oneway, friedmanchisquare, kruskal, levene,
                         mannwhitneyu, wilcoxon)
# -----------------------------------------


class InferencialStats:
    """
    Class which analyze and test one or multiple measures

    Attributes
    ----------
    measures : List of measures lists.

    alpha : Significance level. By default this value is 0.05
            but it can be a value assigned by user.

    is_paired : Parameter that indicates if measures are paired or not.

    mean : Optional value for single measure case to carry out statistic test.

    Returns
    -------
    InferencialStats object : InferencialStats object to analyze and test 
    the measure or measures instaced
    """
    res_print = "Stadistical features:\nStats ::> {}\nP-value ::> {}"
    test_res = "Stadistic Tests"
    pvalue_string = "P value"
    stats_string = "Stats"
    common_stadistics_string = "Common Stadistics"
    normal_string = "Normal Distribution"
    data_string = "Data {}"
    levene_string = "Levene Test"
    shapiro_string = "Shapiro Norm"

    def __init__(self, measures, alpha=0.05, is_paired=False, mean=None):
        """
        Create a new class: InferencialStat instance

        Parameters
        ----------
        measures: List of measures to instance a new InferencialStat object
        alpha : Significance level. By default this value is 0.05
                but it can be a value assigned by user.
        is_paired : Parameter that indicates if measures are paired or not.
        mean : Optional value for single measure case to carry out statistic test.

        Returns
        -------
        New InsferencialStat object
        """
        if type(measures) is not list:
            print(
                "Error: Type of argument[1].\nUse [1]measures: Must be list type")
            quit()
        if len(measures) == 0:
            print(
                "Error: Length of measures.\nUse [1]measures: Must be at least 1 or even more")
            quit()
        if type(is_paired) is not bool:
            print(
                "Error: Type of argument[2].\nUse [2]Pairing: Must be bool type")
            quit()
        if type(alpha) is not float:
            print(
                "Error: Type of argument[3].\nUse [3]alpha: Must be float type")
            quit()
        if mean is not None and (type(mean) != int and type(mean) != float):
            print("Error:\"mean\" type is not correct. Must be \n-int\n-float\n-None")
        self.measures = measures
        self.alpha = alpha
        self.is_paired = is_paired
        self.mean = mean
        self.dictionary_stats = {}

    def inferencial_statistics(self):
        """
        Statistical studies will be carried out for each sample

        Parameters
        ----------
        self.measures : list of measures lists.
                Applies non-parametric tests to obtain stadistical features.

        self.alpha : Significance level. By default this value is 0.05
                but it can be a value assigned by user.

        self.is_paired : Parameter that indicates if measures are paired or not.

        self.mean : Optional value for single measure case to carry out statistic test.

        Returns
        -------
        result : Dictionary
                Stadistical features as the results of analyzing measures
        """

        # not all(isinstance(l, list) for l in measures)
        if len(self.measures) == 1:
            self.single_stadistics(self.measures, self.alpha, self.mean)
        else:
            self.multiple_stadistics(self.measures, self.alpha, self.is_paired)
            # Realización de Bonferroni
            # bonferroni_test(measures, alpha)
        return self.dictionary_stats

    def single_stadistics(self, measure, alpha, mean):
        """
        This method study data recieved by normal or non-normal stadistic tests

        Parameters
        ----------
        measures :
            Input data which will be studied.

        alpha:
            Significance level. By default this value is 0.05 but it can be a value assigned by user.

        mean:
            Optional value to apply stadistical test.
        Returns
        -------
        Dictionary object with test results

        """
        self.dictionary_stats[self.common_stadistics_string] = self.common_stadistics(
            measure, alpha)
        if mean is not None:
            stats_1samp, pvalue_1samp = stats.ttest_1samp(
                np.array(measure[0]), mean)
            self.dictionary_stats["T test"] = {"stat": stats_1samp,
                                               "p-value": pvalue_1samp}

    def multiple_stadistics(self, measures, alpha, is_paired):
        """
        Case that analyze multiple measures
        carrying out multiples stadistical test

        Parameters
        ----------
        measures : list of measures lists.
                Applies non-parametric tests to obtain stadistical features.

        alpha : Significance level. By default this value is 0.05
                but it can be a value assigned by user.

        is_paired : Parameter that indicates if measures are paired or not.

        Returns
        -------
        result : Dictionary
                Stadistical features as the results of analyzing measures
        """

        self.dictionary_stats[self.common_stadistics_string] = self.common_stadistics(
            measures, alpha)
        measure_len = len(measures[0])
        self.dictionary_stats[self.levene_string] = self.homocedasticity(
            measures, alpha)
        if is_paired:
            if any(len(lst) != measure_len for lst in measures):
                print(
                    "Error: Data Length.\nUse isPaired: Each measure must have same length of data")
                raise SystemExit()
            if not self.check_normality():
                print("Normality conditions are not met.\n")
                self.non_parametric_test(measures, is_paired)
            else:
                print("Normality conditions are met.\n")
                self.parametric_test(measures, is_paired)
        else:
            if not self.check_normality():
                print("Normality conditions are not met.\n")
                self.non_parametric_test(measures, is_paired)
            else:
                print("Normality conditions are met.\n")
                self.parametric_test(measures, is_paired)

    def common_stadistics(self, measures, alpha):
        """
        Generate multiple sublopts showing every data histogram stored in
        the fisrt parameter.
        Check if measures from the firteamsst argument have Normal or Non-Normal
        Distribution and store the results within a dictionary.

        Parameters
        ----------
        measures : list of data lists.

        alpha : Signifance level that will be applied in every test.

        Returns
        -------
        result: Dictionary with all stadistical tests evaluated to every data
        """
        dictionary = {}
        norm_list = self.dictionary_stats[self.shapiro_string] = []
        for index, data in enumerate(measures):
            data_test = np.array(data)
            # histogram
            fig_histogram = px.histogram(data_test, marginal="box")
            fig_histogram['layout'].update({
                'title': 'Histogram',
                'showlegend': False,
                'width': 800,
                'height': 800,
            })
            # Qqplot
            qqplot_data = qqplot(data_test, line='s').gca().lines
            fig_qqplot = go.Figure()
            fig_qqplot.add_trace({
                'type': 'scatter',
                'x': qqplot_data[0].get_xdata(),
                'y': qqplot_data[0].get_ydata(),
                'mode': 'markers',
                'marker': {
                    'color': '#19d3f3'
                }
            })
            fig_qqplot.add_trace({
                'type': 'scatter',
                'x': qqplot_data[1].get_xdata(),
                'y': qqplot_data[1].get_ydata(),
                'mode': 'lines',
                'line': {
                    'color': '#636efa'
                }
            })
            fig_qqplot['layout'].update({
                'title': 'Quantile-Quantile Plot',
                'xaxis': {
                    'title': 'Theoritical Quantities',
                    'zeroline': False
                },
                'yaxis': {
                    'title': 'Sample Quantities'
                },
                'showlegend': False,
                'width': 800,
                'height': 800,
            })
            print("Applying Shapiro-Wilk test in Data {}".format(index+1))
            dic_shapiro = self.check_shapiro(data, alpha)
            dictionary[self.data_string.format(index+1)] = {
                'Histogram': fig_histogram.to_json(),
                'Qqplot': fig_qqplot.to_json(),
                'Shapiro Wilk': dic_shapiro
            }
            norm_list.append(dic_shapiro[self.normal_string])
        return dictionary

    def check_shapiro(self, measures, alpha):
        """
        Apply Shapiro-Wilk test to input measures and analyze the result
        comparing pvalue obtained against alpha

        Parameters
        ----------
        measures : list of data lists.

        alpha : Signifance level that will be applied in every test.

        Returns
        -------
        Dictionary with all stadistical tests evaluated to every data
        If pvalue > alpha then Normal Distribution satisfied
        """
        stat, p = stats.shapiro(measures)
        if p > alpha:
            res = True
        else:
            res = False
        res_dic = {
            "Stat": stat,
            self.pvalue_string: p,
            self.normal_string: res
        }
        return res_dic

    def check_normality(self):
        """
        Check if levene and Shapiro-Wilk test's results were satisfied by the
        measure or measures of InferencialStats object.

        Returns
        -------
        Boolean value: True if normality conditions are satisfied.
                        E.O.C the normality conditions are not satisfied
                        then it return False.
        """
        norm_list = self.dictionary_stats[self.shapiro_string]
        res = False
        shapiro_norm = all((value) == True for value in norm_list)
        if self.dictionary_stats[self.levene_string].get("Homogeneity") and shapiro_norm:
            res = True
        return res

    def homocedasticity(self, measures, alpha):
        """
        Use Levene Test with input measures. Then studies the result of
        test comparing pvalue against alpha

        Parameters
        ----------
        measures :
            List of measures to be applied to the Levene's test for
            homocedasticity testing.

        alpha:
            Significance level. By default this value is 0.05 but
            it can be a value assigned by user.

        Returns
        -------
        True : If `pvalue > alpha` homogeneity is then satisfied.

        False : Homogeneity not satisfied

        """
        print("\n\nApplying Levene Test\n")
        dict_res = {}
        stats, p = levene(*measures)
        if p > alpha:
            res = True
        else:
            res = False
        dict_res = {
            "Homogeneity": res,
            "Stats": stats,
            self.pvalue_string: p
        }
        return dict_res

    def parametric_test(self, measures, is_paired):
        """
        Applies `the best case` parametric tests for the samples `measures` obtained
        as parameters.

        Parameters
        ----------
        measures : list of measures lists
                Applies tests to obtain stadistical features

        is_paired : Parameter that indicates if measures are paired or not.

        Returns
        -------
        result : Dictionary
                Stadistical features as the results of manipulate data samples
        """
        print("Applying parametric test")
        arr_measures = np.array(measures, dtype=object)
        if len(measures) < 3:
            if is_paired:
                t_stats, p_value = (arr_measures[0], arr_measures[1])
                print("\n\nRunning T-test \"Between groups\"...\n\n")
                self.dictionary_stats[self.test_res] = {
                    "T-test Between Groups": {
                        self.stats_string: t_stats,
                        self.pvalue_string: p_value
                    }
                }
            else:
                t_stats, p_value = stats.ttest_ind(
                    arr_measures[0], arr_measures[1])
                print("\n\nRunning T-test \"within groups\"...\n\n")
                self.dictionary_stats[self.test_res] = {
                    "T-test Within Groups": {
                        self.stats_string: t_stats,
                        self.pvalue_string: p_value
                    }
                }

        else:
            if is_paired:
                df = self.make_dataframe(arr_measures)
                aovrm = AnovaRM(df, depvar='datas',
                                subject='groups', within=['rows']).fit()
                print("\n\nRunning One Way ANOVA *Repeated Measures*\n\n")
                self.dictionary_stats[self.test_res] = {
                    "One way ANOVA RM": {
                        aovrm.summary()
                    }
                }

            else:
                f_stats, p_value = f_oneway(*arr_measures)
                print("\n\nRunning One Way ANOVA\n\n")
                self.dictionary_stats[self.test_res] = {
                    "One way ANOVA": {
                        self.stats_string: f_stats,
                        self.pvalue_string: p_value
                    }
                }

    def non_parametric_test(self, measures, is_paired):
        """
        Applies `the best case` non-parametric tests for the samples `datas` obtained
        as parameters.

        Parameters
        ----------
        measures : list of measures lists.
                Applies non-parametric tests to obtain stadistical features.

        is_paired : Parameter that indicates if measures are paired or not.

        Returns
        -------
        result : Dictionary
                Stadistical features as the results of manipulate data samples
        """
        print("Applying Non-parametric test")
        arr_measures = np.array(measures, dtype=object)
        if len(measures) < 3:
            # Para 2 muestras
            if is_paired:
                # Aplicamos test de emparejamiento Wilcoxon
                stats, pvalue = wilcoxon(arr_measures[0], arr_measures[1])
                print("\n\nRunning Wilcoxon\n\n")
                self.dictionary_stats[self.test_res] = {
                    "Wilcoxon test": {
                        self.stats_string: stats,
                        self.pvalue_string: pvalue
                    }
                }
            else:
                # Aplicamos test no emparejados
                stats, pvalue = mannwhitneyu(
                    arr_measures[0], arr_measures[1], alternative="two-sided")
                print("\n\nRunning Mannwhitneyu\n\n")
                self.dictionary_stats[self.test_res] = {
                    "Mann-Whitney test": {
                        self.stats_string: stats,
                        self.pvalue_string: pvalue
                    }
                }
        else:
            # Para 3 o + muestras
            if is_paired:
                # Aplicamos test de emparejamiento Friedmann
                stats, pvalue = friedmanchisquare(*arr_measures)
                print("\n\nRunning Friedmanchisquare\n\n")
                self.dictionary_stats[self.test_res] = {
                    "Friedman test": {
                        self.stats_string: stats,
                        self.pvalue_string: pvalue
                    }
                }

            else:
                # Aplicamos test no emparejados Kruskal
                stats, pvalue = kruskal(*arr_measures)
                print("\n\nRunning Kruskal\n\n")
                self.dictionary_stats[self.test_res] = {
                    "Kruskal-Wallis test": {
                        self.stats_string: stats,
                        self.pvalue_string: pvalue
                    }
                }

    def crit_diff(self):
        """
        Display a graphical analisys comparing critical 
        differences from each measures

        Parameters
        ----------
        self.measures : lists of measures.

        self.alpha : Significance level that share all data.

        Returns
        -------
        result : Graphical comparison displaying critical differences
        """
        import math
        if any(len(measure) >= 25 for measure in self.measures):
            print(
                "Error: Measure Length.\nUse measures: Each measure must have less than 25 elements")
            raise SystemExit()
        bon_05 = [0, 1.960, 2.242, 2.394, 2.498, 2.576, 2.639, 2.690, 2.735, 2.773, 2.807, 2.838,
                  2.866, 2.891, 2.914, 2.936, 2.955, 2.974, 2.992, 3.008, 3.024, 3.038, 3.052, 3.066, 3.078]
        bon_10 = [0, 1.645, 1.960, 2.128, 2.242, 2.327, 2.394, 2.450, 2.498, 2.540, 2.576, 2.609,
                  2.639, 2.666, 2.690, 2.713, 2.735, 2.755, 2.773, 2.791, 2.807, 2.823, 2.838, 2.852, 2.866]
        N = len(self.measures)
        k = len(self.measures[0])
        q0_05 = bon_05[k]
        q0_10 = bon_10[k]

        cd0_05 = q0_05 * math.sqrt((k*(k+1))/(6*N))
        cd0_10 = q0_10 * math.sqrt((k*(k+1))/(6*N))

        # Rankings
        ranks = get_ranks(self.measures)
        print("Average Rankings -> {}".format(ranks))
        print("Min Ranking ->{}\n\n".format(min(ranks)))
        ids = ["Measure {}".format(data+1)
               for data in range(len(self.measures))]
        data_df = {
            'Measures': ids,
            'Ranking': ranks
        }
        df = pd.DataFrame(data_df)
        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=df['Measures'],
                y=df['Ranking'],
                name='Ranks',
                text=df['Ranking'],
                textposition='auto'
            )
        )
        fig['layout'].update({
            'title': 'Critical Differences',
            'showlegend': True,
            'width': 800,
            'height': 800
        })
        # Add another trace in the plot to display critical value
        # Check which measure has the min value and then sum min value and critical value
        if(self.alpha == 0.05 or self.alpha == 0.01):
            cd_value_05 = np.full(shape=len(ranks),
                                  fill_value=(min(ranks)+cd0_05))
            cd_value_10 = np.full(shape=len(ranks),
                                  fill_value=(min(ranks)+cd0_10))
            fig.add_trace(go.Scatter(
                x=df['Measures'],
                y=cd_value_05,
                name="0.05",
                line=dict(color='firebrick', width=4, dash='dot')))
            fig.add_trace(go.Scatter(
                x=df['Measures'],
                y=cd_value_10,
                name="0.01",
                line=dict(color='green', width=4, dash='dot')))
        fig.show()
        return [cd0_05, cd0_10]

    def make_dataframe(self, data_frames):
        """
        Create panda dataframer from one or more lists/array-like datas
        to be tested in ANOVA test

        Parameters
        ----------
        data_frames : list of data lists

        Returns
        -------
        result : Panda Dataframe
        """
        import itertools

        len_groups = len(data_frames[0])
        datas = list(itertools.chain(*data_frames))

        groups = list()
        for i in range(len(data_frames)):
            groups += (["data {}".format(i+1)] * len_groups)

        rows = np.arange(len_groups).tolist()*len(data_frames)
        dictionary = {"datas": datas, "groups": groups, "rows": rows}
        df = pd.DataFrame(dictionary, columns=['datas', 'groups', 'rows'])
        return df

    def get_hists(self):
        """
        Get all histograms obtained

        Returns
        -------
        result : Histograms of all measures
        """
        hists = []
        local_result = self.dictionary_stats[self.common_stadistics_string]
        for i in range(len(local_result)):
            hists.append(
                pio.from_json(
                    local_result[self.data_string.format(i+1)]["Histogram"]
                )
            )
        return hists

    def get_hist(self, index):
        """
        Get and show histogram of measure requested

        Parameters
        ----------
        index : Histogram position requested
        All measures are identified initializing with 1.

        Returns
        -------
        plotly.graph_objects.Figure : Histogram of measures requested
        """
        hist_res = None
        local_result = self.dictionary_stats[self.common_stadistics_string]
        if index <= len(local_result):
            hist_res = pio.from_json(
                local_result[self.data_string.format(index+1)]["Histogram"]
            )
            hist_res.show()
        return hist_res

    def show_hists(self):
        """
        Show a figure with all measure histograms

        Returns
        -------
        plotly.graph_objects.Figure : All histograms of each measure analyzed
        """
        fig = go.Figure()
        if len(self.measures) == 1:
            hist_data = np.array(self.measures[0])
            fig.add_trace(go.Histogram(x=hist_data))
        else:
            r = 1
            c = 1
            rows = 2+len(self.measures) % 2
            columns = len(self.measures)//2
            measure_names = ["Histogram {}".format(
                i+1) for i in range(len(self.measures))]
            fig = make_subplots(rows=rows, cols=columns,
                                subplot_titles=measure_names)
            for i in range(len(self.measures)):
                hist_data = np.array(self.measures[i])
                fig.add_trace(go.Histogram(
                    x=hist_data,
                    name="Histogram {}".format(i+1)
                ),
                    row=r,
                    col=c,
                )
                if(c < columns):
                    c = c+1
                else:
                    c = 1
                    r = r+1
        fig['layout'].update({
            'title': 'Histogram',
            'showlegend': True,
        })
        fig.show()

    def get_qqplots(self):
        """
        Get all QQplots obtained

        Returns
        -------
        result : QQplot of all measures
        """
        qqplot_res = []
        local_result = self.dictionary_stats[self.common_stadistics_string]
        for i in range(len(local_result)):
            qqplot_res.append(
                pio.from_json(
                    local_result[self.data_string.format(i+1)]["Qqplot"]
                )
            )
        return qqplot_res

    def get_qqplot(self, index):
        """
        Get and show histogram of measure requested

        Parameters
        ----------
        index : Histogram position requested
        All measures are identified initializing with 1.

        Returns
        -------
        result : Histogram of measures requested
        """
        qqplot_res = None
        local_result = self.dictionary_stats[self.common_stadistics_string]
        if index <= len(local_result):
            qqplot_res = pio.from_json(
                local_result[self.data_string.format(index+1)]["Qqplot"]
            )
            qqplot_res.show()
        return qqplot_res

    def show_qqplots(self):
        """
        Show a figure with all measure qqplots

        Returns
        -------
        plotly.graph_objects.Figure : All qqplots of each measure analyzed
        """
        fig = go.Figure()
        if len(self.measures) == 1:
            qq_data = np.array(self.measures[0])
            qqplot_data = qqplot(qq_data, line='s').gca().lines
            fig.add_trace({
                'type': 'scatter',
                'x': qqplot_data[0].get_xdata(),
                'y': qqplot_data[0].get_ydata(),
                'mode': 'markers',
                'marker': {
                    'color': '#19d3f3'
                },
                'name': "QQplot 1"
            })
            fig.add_trace({
                'type': 'scatter',
                'x': qqplot_data[1].get_xdata(),
                'y': qqplot_data[1].get_ydata(),
                'mode': 'lines',
                'line': {
                    'color': '#636efa'
                }
            })
        else:
            r = 1
            c = 1
            rows = 2+len(self.measures) % 2
            columns = len(self.measures)//2
            measure_names = ["QQplot {}".format(
                i+1) for i in range(len(self.measures))]
            fig = make_subplots(rows=rows, cols=columns,
                                subplot_titles=measure_names)
            for i in range(len(self.measures)):
                qq_data = np.array(self.measures[i])
                qqplot_data = qqplot(qq_data, line='s').gca().lines
                fig.add_trace({
                    'type': 'scatter',
                    'x': qqplot_data[0].get_xdata(),
                    'y': qqplot_data[0].get_ydata(),
                    'mode': 'markers',
                    'marker': {
                        'color': '#19d3f3'
                    },
                    'name': "Plot {}".format(i+1)
                },
                    row=r,
                    col=c)
                fig.add_trace({
                    'type': 'scatter',
                    'x': qqplot_data[1].get_xdata(),
                    'y': qqplot_data[1].get_ydata(),
                    'mode': 'lines',
                    'line': {
                        'color': '#636efa'
                    },
                    'showlegend': False
                },
                    row=r,
                    col=c)
                if(c < columns):
                    c = c+1
                else:
                    c = 1
                    r = r+1
        fig['layout'].update({
            'title': 'Quantile-Quantile Plot'
        })
        fig.show()

    def get_swtests(self):
        """
        Get all Shapiro-Wilk tests obtained

        Returns
        -------
        result : All Shapiro-Wilk test results of all measures.
        """
        stats_list = []
        pvalue_list = []
        norm_cond_list = []
        shap_string = "Shapiro Wilk"
        local_result = self.dictionary_stats[self.common_stadistics_string]
        for i in range(len(local_result)):
            stats_list.append(
                local_result[self.data_string.format(i+1)][shap_string]["Stat"]
            )
            pvalue_list.append(
                local_result[self.data_string.format(
                    i+1)][shap_string]["P value"]
            )
            norm_cond_list.append(
                local_result[self.data_string.format(i+1)][shap_string]
                [self.normal_string]
            )
        df_data = {
            "Stat": stats_list,
            "Pvalue": pvalue_list,
            "Normality condition": norm_cond_list
        }
        df = pd.DataFrame(df_data)
        return df

    def get_swtest(self, index):
        """
        Get Shapiro-Wil test result of measure requested.

        Parameters
        ----------
        results : Variable which store commons stadistics results.
        index : Shapiro-Wilk test position requested.
        All measures are identified initializing with 1.

        Returns
        -------
        result : Shapiro-Wilk test of measures requested.
        """
        sw_res = None
        local_result = self.dictionary_stats[self.common_stadistics_string]
        if index <= len(local_result):
            sw_res = local_result[
                "Data {}".format(index+1)]["Shapiro Wilk"]
        return sw_res

    def get_levene_res(self):
        """
        Get results of levene test.

        Returns
        -------
        result : Dicitionary with the results of levene test.
        """
        return self.dictionary_stats[self.levene_string]

    def get_st_res(self):
        """
        Get parametric or non parametric results.

        Returns
        -------
        result : Dicitionary with the results stadistics test.
        """
        return self.dictionary_stats[self.test_res]

    def get_t_res(self):
        """
        Get t test results in case of one measure.

        Returns
        -------
        result : Dicitionary with the results stadistics test.
        """
        df_data = {
            "Stat": [self.dictionary_stats["T test"]["stat"]],
            "Pvalue": [self.dictionary_stats["T test"]["p-value"]],
        }
        df = pd.DataFrame(df_data)
        return df


def get_ranks(measures):
    """
    Get ranks of input measures.

    Returns
    -------
    result : List of average rankings for each sample
    """
    list_transpose = np.transpose(measures)
    ranks = []
    for x in range(len(list_transpose)):
        series = pd.Series(list_transpose[x]).rank()
        ranks.append(series.tolist())
    ranks_transpose = np.transpose(ranks)
    ranks_mean = [rank.mean() for rank in ranks_transpose]
    return ranks_mean
