import pytest
import avocado_price_predictor_model.predict as predictor


@pytest.fixture
def data():
    return {
        'sold_plu_4046': 5,
        'sold_plu_4225': 6,
        'sold_plu_4770': 8,
        'small_bags': 4,
        'large_bags': 0,
        'xlarge_bags': 0,
        'organic': True,
        'region': 'Albany',
        'date': '2020-12-27'
    }


def test_create_data_frame(data):
    x = predictor._create_avocado_data_frame(data)
    assert x is not None
    assert hasattr(x, 'columns')
    assert len(x.columns) == len(data)


def test_prediction_ok(data):
    y = predictor.predict(data)
    assert type(y) == float


def test_create_data_frame_empty_data():
    x = predictor._create_avocado_data_frame({})
    assert x is None


def test_prediction_empty_data():
    y = predictor.predict({})
    assert y == 0


def test_create_data_frame_missing_data(data):
    del data['small_bags']
    x = predictor._create_avocado_data_frame(data)
    assert x is None


def test_prediction_missing_data(data):
    del data['small_bags']
    y = predictor.predict(data)
    assert y == 0


def test_create_data_frame_invalid_date(data):
    data['date'] = 'invalid'
    x = predictor._create_avocado_data_frame(data)
    assert x is None


def test_prediction_invalid_date(data):
    data['date'] = 'invalid'
    y = predictor.predict(data)
    assert y == 0


def test_create_data_frame_invalid_type(data):
    data['organic'] = 'invalid'
    x = predictor._create_avocado_data_frame(data)
    assert x is None


def test_prediction_invalid_type(data):
    data['organic'] = 'invalid'
    y = predictor.predict(data)
    assert y == 0


def test_create_data_frame_oov_region(data):
    data['region'] = 'oov'
    x = predictor._create_avocado_data_frame(data)
    assert x is not None
    assert hasattr(x, 'columns')
    assert len(x.columns) == len(data)


def test_prediction_oov_region(data):
    data['region'] = 'oov'
    y = predictor.predict(data)
    assert y == 0
