# ---------- requirements ----------
from scipy.sparse import isspmatrix

# local reqs
from vizcovidfr.maps import maps
from vizcovidfr.sparse import sparse
from vizcovidfr.regression import regression
from vizcovidfr.line_charts import line_charts
from vizcovidfr.barplots import barplots
from vizcovidfr.pie_charts import pie_chart
from vizcovidfr.prediction import prediction
from vizcovidfr.heatmaps import heatmap


# ---------- maps ----------
def test_viz2Dmap():
    """
    Test viz2Dmap by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_chiffres_cles().save_as_df()
        - preprocess_chiffres_cles.drop_some_columns()
        - preprocess_chiffres_cles.reg_depts()
        - preprocess_chiffres_cles.reg_depts_code_format()
        - preprocess_maps.map_save_path_routine()
    """
    result = (type(maps.viz2Dmap(file_path='')) != int)
    assert result


def test_viz3Dmap():
    """
    Test viz3Dmap by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_chiffres_cles().save_as_df()
        - preprocess_chiffres_cles.drop_some_columns()
        - preprocess_chiffres_cles.reg_depts()
        - preprocess_chiffres_cles.reg_depts_code_format()
        - preprocess_maps.map_save_path_routine()
    """
    result = (type(maps.viz3Dmap(file_path='')) != int)
    assert result


def test_transfer_map():
    """
    Test transfer_map by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_transfer().save_as_df()
        - preprocess_maps.map_save_path_routine()
    """
    result = (type(maps.transfer_map(file_path='')) != int)
    assert result


def test_vacmap():
    """
    Test vacmap by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will be raised
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_vaccination().save_as_df()
        - preprocess_maps.map_save_path_routine()
    """
    result = (type(maps.vacmap(file_path='')) != int)
    assert result


# ---------- sparse ----------
def test_sparse_graph():
    """
    Test sparse_graph. Call the function and check if the number of edges
    of the resulting graph is an integer.
    If not, an AssertionError will raise.
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_transfer().save_as_df()
    """
    G = sparse.sparse_graph(show=False)
    e = G.number_of_edges()
    result = (type(e) == int)
    assert result


def test_sparse_matrix():
    """
    Test sparse_matrix. Call the function and check if the resulting matrix
    is a sparse matrix.
    If not, an AssertionError will raise.
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_transfer().save_as_df()
    """
    result = (isspmatrix(sparse.sparse_matrix(show=False)))
    assert result


# ---------- regression ----------
def test_scatter_reg():
    """
    Test scatter_reg by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(regression.scatter_reg(1, 1)) != int)
    assert result


def test_poly_fit():
    """
    Test poly_fit by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(regression.poly_fit(1, 1)) != int)
    assert result


def test_R2():
    """
    Test R2 by running the function checking if R2 is different of 2.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(regression.R2(1, 1)) != 2)
    assert result


# ---------- line charts ----------
def test_vactypedoses():
    """
    Test vactypedoses by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will be raised
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_Vaccine_storage().save_as_df()
    """
    result = (type(line_charts.vactypedoses()) != int)
    assert result


def test_vacdoses():
    """
    Test vacdoses by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will be raised
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_Vaccine_storage().save_as_df()
    """
    result = (type(line_charts.vacdoses()) != int)
    assert result


def test_keytimeseries():
    """
    Test keyseries by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will be raised
    """
    result = (type(line_charts.keytimeseries()) != int)
    assert result


# ----------- barplots ---------------
def test_bar_age():
    """
    Test bar_age by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(barplots.bar_age(1, 1)) != int)
    assert result


def test_bar_reg():
    """
    Test bar_reg by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(barplots.bar_reg(1)) != int)
    assert result


def test_compareMF():
    """
    Test compareMF by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(
                barplots.compareMF(date='2020-11-12',
                                   criterion='P',
                                   granularity='France')) != int)
    assert result


# ----------- pie chart ---------------
def test_piechart():
    """
    Test piechart by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    ---
    Functions/methods that will be tested by extension:
        - load_datasets.Load_chiffres_cles().save_as_df()
        - preprocess_chiffres_cles.drop_some_columns()
        - preprocess_chiffres_cles.reg_depts()
    """
    result = (type(pie_chart.piechart()) != int)
    assert result


# --------------prediction--------------
def test_predict_curve():
    """
    Test predict_curve by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(prediction.predict_curve(1, 1, '2021-08-01', show=False)) != float)
    assert result


def test_predict_value():
    """
    Test predict_value by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(prediction.predict_value(1, 1, '2021-08-01')) != int)
    assert result


# --------------heatmaps--------------
def test_heatmap_age():
    """
    Test heatmap_age by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(heatmap.heatmap_age(start='2021-03')) != int)
    assert result


def test_heatmap_reg_age():
    """
    Test heatmap_reg_age by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(heatmap.heatmap_reg_age("2020-S35")) != int)
    assert result


def test_heatmap_reg_day():
    """
    Test heatmap_reg_day by running the function.
    If something fails while running it, result won't be defined,
    and an AssertionError will raise.
    """
    result = (type(heatmap.heatmap_reg_day(0, '2020-11-11',
                                           '2020-11-30', 'daily')) != int)
    assert result
