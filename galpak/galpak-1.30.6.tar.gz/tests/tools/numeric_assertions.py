import math


class NumericAssertions:
    """
    This class is a mixin following the UnitTest naming conventions.
    It is meant to be used along with unittest.TestCase like so :
    class MyTest(unittest.TestCase, NumericAssertions):
        ...
    It needs python >= 2.6
    """

    def assertIsNan(self, value, msg=None):
        """
        Fail if provided value is not nan
        """
        standardMsg = "%s is not nan" % str(value)
        try:
            if not math.isnan(value):
                self.fail(self._formatMessage(msg, standardMsg))
        except:
            self.fail(self._formatMessage(msg, standardMsg))

    def assertIsNotNan(self, value, msg=None):
        """
        Fail if provided value is nan
        """
        standardMsg = "Provided value is nan"
        try:
            if math.isnan(value):
                self.fail(self._formatMessage(msg, standardMsg))
        except:
            pass