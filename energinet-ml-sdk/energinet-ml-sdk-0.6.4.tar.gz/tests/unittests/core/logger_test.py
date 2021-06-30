import pytest

from energinetml.core.logger import MetricsLogger


@pytest.fixture
def logger():
    yield MetricsLogger()


class TestMetricsLogger:

    def test__echo(self, logger):
        """
        :param MetricsLogger logger:
        """
        with pytest.raises(NotImplementedError):
            logger.echo('s')

    def test__log(self, logger):
        """
        :param MetricsLogger logger:
        """
        with pytest.raises(NotImplementedError):
            logger.log('name', 'value')

    def test__tag(self, logger):
        """
        :param MetricsLogger logger:
        """
        with pytest.raises(NotImplementedError):
            logger.tag('key', 'value')

    def test__dataframe(self, logger):
        """
        :param MetricsLogger logger:
        """
        with pytest.raises(NotImplementedError):
            logger.dataframe('name', 'df')
