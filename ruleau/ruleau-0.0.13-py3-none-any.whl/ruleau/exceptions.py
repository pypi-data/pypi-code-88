class RuleRequiresNameException(Exception):
    """Exception raised if a rule doesn't have a human readable name"""


class RuleRequiresIdException(Exception):
    """Exception raised if rule doesn't have an id"""


class MethodNotAllowedException(Exception):
    """Exception raised if a forbidden RuleauDict method is called"""


class CaseIdRequiredException(Exception):
    """Exception raised if a json path for case identifier is not found"""


class CannotOverrideException(Exception):
    """Exception raised if a API tries to override a rule marked as NO_OVERRIDE"""


class DuplicateRuleNameException(Exception):
    """Exception raised if more than 1 rule has same name"""


class RuleIdIllegalCharacterException(Exception):
    """Exception raise if Rule name contains illegal characters"""


class DuplicateRuleIdException(Exception):
    """Exception raised if more than 1 rule has same name"""


class APIException(Exception):
    """Generic exception for API request failure"""
