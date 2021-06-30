import click

from cloudrail.cli.api_client.cloudrail_api_client import CloudrailApiClient
from cloudrail.cli.cli_configuration import CliConfiguration
from cloudrail.cli.commands_utils import API_KEY_HELP_MESSAGE
from cloudrail.cli.service.cloudrail_cli_service import CloudrailCliService
from cloudrail.cli.service.evaluation_run_command_service import EvaluationRunCommandService, GenerateFilteredPlanCommandParameters
from cloudrail.cli.terraform_service.terraform_context_service import TerraformContextService
from cloudrail.cli.terraform_service.terraform_plan_converter import TerraformPlanConverter
from common.api.dtos.assessment_job_dto import RunOriginDTO
from common.api.dtos.cloud_provider_dto import CloudProviderDTO


@click.command(short_help='Generate the filtered Terraform plan to be used with \'run\' and save for analysis.'
                          ' This filtered plan can later be provided to \'run\'',
               help='Generate a filtered Terraform plan from a full Terraform plan. This context will not be uploaded '
                    'to the Cloudrail Service yet. You can review it before uploading, and then use the \'run\' command with the'
                    ' \'--filtered-plan\' parameter (instead of the \'--tf-plan\' parameter).')
@click.option("--tf-plan",
              help='The file path that was used in "terraform plan -out=file" call',
              prompt='Enter Terraform plan file path',
              type=click.STRING)
@click.option("--directory",
              help='The root directory of the .tf files - the same directory where you would run "terraform init". '
                   'If omitted, Cloudrail will attempt to determine it automatically by looking for the \'.terraform\' directory.',
              type=click.STRING)
@click.option('--origin',
              help='Where is Cloudrail being used - on a personal "workstation" or in a "ci" environment.',
              type=click.STRING,
              default=RunOriginDTO.WORKSTATION)
@click.option("--output-file",
              help='The file to save the results to. If left empty, results will appear in STDOUT.',
              type=click.STRING,
              default='')
@click.option("--api-key",
              help=API_KEY_HELP_MESSAGE,
              type=click.STRING)
@click.option('--notty',
              help='Use non-interactive mode',
              type=click.BOOL,
              is_flag=True,
              default=False)
@click.option('--upload-log',
              help='Upload log in case of failure',
              type=click.BOOL,
              is_flag=True,
              default=False)
@click.option('--no-upload-log',
              help='Do not upload logs in case of failure',
              type=click.BOOL,
              is_flag=True,
              default=False)
@click.option("--cloud-provider",
              help='cloud provider name, i.e aws/azure',
              type=click.Choice(['AWS', 'Azure'], case_sensitive=False),
              default=None)
@click.option("--base-dir",
              help='When printing the locations of code files, Cloudrail will prepend this path',
              type=click.STRING,
              default='')
# pylint: disable=W0613
def generate_filtered_plan(directory: str, tf_plan: str, origin: str, output_file: str, api_key: str, notty: bool,
                           upload_log: bool, no_upload_log: bool, cloud_provider: str, base_dir: str):
    """
    Send Terraform out file to Cloudrail service for evaluation. We are getting back
    job_id and checking every X sec if the evaluation is done, once the evaluati
    """
    api_client = CloudrailApiClient()
    cloudrail_repository = CloudrailCliService(api_client, CliConfiguration())
    terraform_environment_context_service = TerraformContextService(TerraformPlanConverter())
    if cloud_provider:
        cloud_provider = CloudProviderDTO.AMAZON_WEB_SERVICES if cloud_provider.lower() == 'aws' else CloudProviderDTO.AZURE
    run_command_service = EvaluationRunCommandService(cloudrail_repository,
                                                      terraform_environment_context_service,
                                                      GenerateFilteredPlanCommandParameters(None,
                                                                                            upload_log,
                                                                                            no_upload_log,
                                                                                            origin,
                                                                                            directory,
                                                                                            tf_plan, output_file,
                                                                                            api_key,
                                                                                            notty,
                                                                                            cloud_provider,
                                                                                            base_dir), 'generate_filtered_plan')

    run_command_service.generate_filtered_plan()
