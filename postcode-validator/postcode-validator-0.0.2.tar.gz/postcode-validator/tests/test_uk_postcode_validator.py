import pytest
from uk.uk_postcode_validator import UKPostcode
from Exceptions.exceptions import ValidationError


@pytest.mark.parametrize(
    "value",
    (
        ("EC1A 1BB"),
        ("W1A 0AX"),
        ("M1 1AE"),
        ("B33 8TH"),
        ("CR2 6XH"),
        ("DN55 1PT"),
    ),
)
def test_uppercase_postcodes(value):
    assert UKPostcode(value).postcode == value


@pytest.mark.parametrize(
    "value",
    (
        ("EC1A 1BB"),
        ("W1A 0AX"),
        ("M1 1AE"),
        ("B33 8TH"),
        ("CR2 6XH"),
        ("DN55 1PT"),
    ),
)
def test_lowercase_postcodes(value):
    assert UKPostcode(value.lower()).postcode == value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A1BB", "EC1A 1BB"),
        ("EC1A 1BB", "EC1A 1BB"),
        ("EC1A  1BB", "EC1A 1BB"),
        ("EC1A   1BB", "EC1A 1BB"),
    ),
)
def test_spacing(input, expected_value):
    assert UKPostcode(input).postcode == expected_value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A 1BB", "EC1A"),
        ("W1A 0AX", "W1A"),
        ("M1 1AE", "M1"),
        ("B33 8TH", "B33"),
        ("CR2 6XH", "CR2"),
        ("DN55 1PT", "DN55"),
    ),
)
def test_outwardcode(input, expected_value):
    assert UKPostcode(input).outward_code == expected_value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A 1BB", "1BB"),
        ("W1A 0AX", "0AX"),
        ("M1 1AE", "1AE"),
        ("B33 8TH", "8TH"),
        ("CR2 6XH", "6XH"),
        ("DN55 1PT", "1PT"),
    ),
)
def test_inwardcode(input, expected_value):
    assert UKPostcode(input).inward_code == expected_value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A 1BB", "EC"),
        ("W1A 0AX", "W"),
        ("M1 1AE", "M"),
        ("B33 8TH", "B"),
        ("CR2 6XH", "CR"),
        ("DN55 1PT", "DN"),
    ),
)
def test_area(input, expected_value):
    assert UKPostcode(input).area == expected_value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A 1BB", "1A"),
        ("W1A 0AX", "1A"),
        ("M1 1AE", "1"),
        ("B33 8TH", "33"),
        ("CR2 6XH", "2"),
        ("DN55 1PT", "55"),
    ),
)
def test_district(input, expected_value):
    assert UKPostcode(input).district == expected_value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A 1BB", "1"),
        ("W1A 0AX", "0"),
        ("M1 1AE", "1"),
        ("B33 8TH", "8"),
        ("CR2 6XH", "6"),
        ("DN55 1PT", "1"),
    ),
)
def test_sector(input, expected_value):
    assert UKPostcode(input).sector == expected_value


@pytest.mark.parametrize(
    "input, expected_value",
    (
        ("EC1A 1BB", "BB"),
        ("W1A 0AX", "AX"),
        ("M1 1AE", "AE"),
        ("B33 8TH", "TH"),
        ("CR2 6XH", "XH"),
        ("DN55 1PT", "PT"),
    ),
)
def test_unit(input, expected_value):
    assert UKPostcode(input).unit == expected_value


@pytest.mark.parametrize(
    "value",
    (
        ("EC1A 1B"),
        ("W1A 0A"),
        ("M1 1A"),
        ("B33 8T"),
        ("CR2 6X"),
        ("DN55 1P"),
    ),
)
def test_invalid_postcodes(value):
    try:
        UKPostcode(value)
        assert False
    except ValidationError:
        assert True
