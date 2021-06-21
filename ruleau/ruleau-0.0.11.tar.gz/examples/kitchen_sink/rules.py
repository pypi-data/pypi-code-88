from ruleau import All, OverrideLevel, rule


@rule(rule_id="rul_01", name="kyc_threshold", override_level=OverrideLevel.NO_OVERRIDE)
def kyc_risk_greater_than_threshold(_, payload):
    """
    Know Your Customer (KYC) score must be greater than the threshold,
    in this case greater than `LOW`

    :Override Guidance: kyc_threshold to mark this failure into review

    >>> kyc_risk_greater_than_threshold(None, {"data": {"kyc": "HIGH"}})
    False
    >>> kyc_risk_greater_than_threshold(None, {"data": {"kyc": "LOW"}})
    True
    """
    return payload["data"]["kyc"] == "LOW"


@rule(rule_id="rul_02", name="fico_score")
def fico_score_greater_than_threshold(_, payload):
    """
    FICO score must be greater than 630

    :Owner: Penny Farthing
    :Override Guidance: Feel free to override in almost any circumstance

    >>> fico_score_greater_than_threshold(None, {"data": {"fico_score": 400}})
    False
    >>> fico_score_greater_than_threshold(None, {"data": {"fico_score": 630}})
    False
    >>> fico_score_greater_than_threshold(None, {"data": {"fico_score": 650}})
    True
    """
    return payload["data"]["fico_score"] > 630


@rule(rule_id="rul_03", name="no_ccjs")
def has_no_ccjs(_, payload):
    """
    Make sure customer has no county court judgements
    >>> has_no_ccjs(None, {"data": {"ccjs": []}})
    True
    >>> has_no_ccjs(None, {"data": {"ccjs": ["Example CCJ"]}})
    False
    >>> has_no_ccjs(None, {"data": {"ccjs": [{"example": "CCJ Object"}]}})
    False
    """
    return len(payload["data"]["ccjs"]) == 0


will_lend = All(
    "rul_04",
    "Top level",
    kyc_risk_greater_than_threshold,
    fico_score_greater_than_threshold,
    has_no_ccjs,
)

from ruleau import ApiAdapter, execute

if __name__ == "__main__":
    result = execute(
        will_lend,
        {"data": {"fico_score": 150, "ccjs": [], "kyc": "low"}},
        api_adapter=ApiAdapter(base_url="http://127.0.0.1:8000"),
        case_id="132",
    )
    print("Result", result.result)
