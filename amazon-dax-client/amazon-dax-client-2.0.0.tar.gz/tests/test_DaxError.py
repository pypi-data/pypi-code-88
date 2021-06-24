from amazondax.DaxError import DaxServiceError, DaxClientError, DaxErrorCode, is_retryable, is_retryable_with_backoff


def test_client_error():
    error = DaxClientError("Something went wrong.",
                           DaxErrorCode.Decoder)
    assert error.code == DaxErrorCode.Decoder
    assert error.codes == None
    assert error.http_status == None


def test_service_error_throttle():
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 37, 38, 39, 50], 1234, None, None)
    assert error.code == DaxErrorCode.Throttling
    assert error.codes == [4, 37, 38, 39, 50]
    assert error.wait_for_recovery_before_retry == False


def test_service_error_recovery():
    error = DaxServiceError(None,
                            "Something went wrong.", [2, 1, 51], 1234, None, None)
    assert error.code == None
    assert error.codes == [2, 1, 51]
    assert error.wait_for_recovery_before_retry == True
    assert error.auth_error == False


def test_service_error_auth():
    error = DaxServiceError(None,
                            "Something went wrong.", [4, 23, 31, 32], 1234, None, None)
    assert error.code == None
    assert error.codes == [4, 23, 31, 32]
    assert error.wait_for_recovery_before_retry == False
    assert error.auth_error == True


def test_is_retryable_not_dax_error():
    error = Exception
    assert is_retryable(error) == False


def test_is_retryable_with_backoff_not_dax_error():
    error = Exception
    assert is_retryable_with_backoff(error) == False


# Errors for testing retryability methods
error1 = DaxServiceError(None,
                         "Something went wrong.", [4, 37, 38, 39, 50], 1234, None, None)
error2 = DaxClientError("Something went wrong.",
                        DaxErrorCode.Decoder)
error3 = DaxServiceError(None,
                         "Something went wrong.", [4, 37, 38, 39, 47], 1234, None, None)
error4 = DaxServiceError(None,
                         "Something went wrong.", [], 1234, None, 500)
error5 = DaxServiceError(None,
                         "Something went wrong.", [], 1234, None, 429)


def test_is_retryable():
    assert is_retryable(error1) == True
    assert is_retryable(error2) == False
    assert is_retryable(error3) == True
    assert is_retryable(error4) == True
    assert is_retryable(error5) == True


def test_is_retryable_with_backoff():
    assert is_retryable_with_backoff(error1) == True
    assert is_retryable_with_backoff(error2) == False
    assert is_retryable_with_backoff(error4) == False
    assert is_retryable_with_backoff(error5) == True
