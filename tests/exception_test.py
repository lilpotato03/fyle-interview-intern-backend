import pytest
from core.libs.exceptions import FyleError

def test_fyle_error_initialization():
    message = "An error occurred"
    status_code = 404
    error = FyleError(status_code=status_code, message=message)

    assert error.status_code == status_code
    assert error.message == message

def test_fyle_error_to_dict():
    message = "An error occurred"
    status_code = 400
    error = FyleError(status_code=status_code, message=message)

    expected_dict = {'message': message}
    assert error.to_dict() == expected_dict

def test_fyle_error_default_status_code():
    message = "Default status code"
    error = FyleError(status_code=FyleError.status_code, message=message)

    assert error.status_code == FyleError.status_code



def test_fyle_error_with_different_status_codes():
    for status_code in [200, 404, 500]:
        error = FyleError(status_code=status_code, message="Error with status code")
        assert error.status_code == status_code
