import pytest
from postcode_validator.Exceptions.exceptions import ValidationError


def test_exception():
    with pytest.raises(ValidationError, match="Postcode is invalid"):
        raise ValidationError("Postcode is invalid")
