from click.testing import CliRunner
from unittest.mock import patch, Mock

from energinetml.core.model import TrainedModel
from energinetml.cli.model.train import train


class TestModelTrain:

    @patch('energinetml.cli.model.train.backend')
    def test__model_not_implemented__should_abort(
            self, backend_mock, model_path):
        """
        :param Mock backend_mock:
        :param str model_path:
        """
        runner = CliRunner()

        context = Mock()
        context.train_model.side_effect = NotImplementedError
        context.get_tags.return_value = {}
        context.get_parameters.return_value = {}
        backend_mock.get_local_training_context.return_value = context

        # Act
        result = runner.invoke(
            cli=train,
            args=['--path', model_path],
        )

        # Assert
        assert result.exit_code == 1
        assert (
            'The train() method of your model raised a NotImplementedError '
            'which indicates that you have not yet implemented it.'
        ) in result.output

    @patch('energinetml.cli.model.train.backend')
    def test__model_returned_something_other_than_trained_model__should_abort(
            self, backend_mock, model_path):
        """
        :param Mock backend_mock:
        :param str model_path:
        """
        runner = CliRunner()

        context = Mock()
        context.train_model.return_value = 'not a TrainedModel object'
        context.get_tags.return_value = {}
        context.get_parameters.return_value = {}
        backend_mock.get_local_training_context.return_value = context

        # Act
        result = runner.invoke(
            cli=train,
            args=['--path', model_path],
        )

        # Assert
        assert result.exit_code == 1
        assert (
            'The object returned by your train()-method must be of type '
            'TrainedModel (or inherited classes).'
        ) in result.output

    @patch('energinetml.cli.model.train.backend')
    @patch('energinetml.cli.model.train.TrainedModel', new=Mock)
    def test__trained_model_does_not_verify__should_abort(
            self, backend_mock, model_path):
        """
        :param Mock backend_mock:
        :param str model_path:
        """
        runner = CliRunner()

        trained_model = Mock()
        trained_model.Invalid = TrainedModel.Invalid
        trained_model.verify.side_effect = TrainedModel.Invalid

        context = Mock()
        context.train_model.return_value = trained_model
        context.get_tags.return_value = {}
        context.get_parameters.return_value = {}
        backend_mock.get_local_training_context.return_value = context

        # Act
        result = runner.invoke(
            cli=train,
            args=['--path', model_path],
        )

        # Assert
        assert result.exit_code == 1
        assert 'does not validate' in result.output

    @patch('energinetml.cli.model.train.backend')
    @patch('energinetml.cli.model.train.TrainedModel', new=Mock)
    def test__should_dump_trained_model_correctly(
            self, backend_mock, model_path):
        """
        :param Mock backend_mock:
        :param str model_path:
        """
        runner = CliRunner()

        trained_model = Mock()

        context = Mock()
        context.train_model.return_value = trained_model
        context.get_tags.return_value = {}
        context.get_parameters.return_value = {}
        backend_mock.get_local_training_context.return_value = context

        # Act
        result = runner.invoke(
            cli=train,
            args=['--path', model_path],
        )

        # Assert
        assert result.exit_code == 0

        trained_model.dump.assert_called_once()
        context.save_output_files.assert_called_once()
