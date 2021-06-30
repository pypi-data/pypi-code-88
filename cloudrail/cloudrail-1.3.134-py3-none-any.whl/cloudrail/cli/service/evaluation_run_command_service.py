import base64
import importlib
import inspect
import logging
import os
import re
import sys
import zlib
from dataclasses import dataclass
from time import time, sleep
from typing import List, Optional

import click
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.data import JsonLexer
from pygments.styles.monokai import MonokaiStyle
from tabulate import tabulate

from cloudrail.knowledge.rules.base_rule import BaseRule
from cloudrail.cli.api_client.external_api_client import ExternalApiClient
from cloudrail.cli.commands_utils import echo_error, validate_origin, validate_input_paths, exit_with_code, validate_cloud_account_input
from cloudrail.cli.error_messages import generate_failure_message, generate_convert_terraform_plan_to_json_failure_message, \
    generate_process_plan_json_failure_message, generate_simple_message
from cloudrail.cli.exit_codes import ExitCode
from cloudrail.cli.result_formatter.json_formatter import JsonFormatter
from cloudrail.cli.result_formatter.json_gitlab_sast_formatter import JsonGitLabSastFormatter
from cloudrail.cli.result_formatter.junit_formatter import JunitFormatter
from cloudrail.cli.result_formatter.sarif_formatter import SarifFormatter
from cloudrail.cli.result_formatter.text_formatter import TextFormatter
from cloudrail.cli.service.cloudrail_cli_service import CloudrailCliService
from cloudrail.cli.service.command_service import CommandParameters, CommandService
from cloudrail.cli.spinner_wrapper import SpinnerWrapper
from cloudrail.cli.terraform_service.terraform_context_service import TerraformContextService
from common.api.dtos.account_config_dto import AccountConfigDTO, AccountStatusDTO
from common.api.dtos.assessment_job_dto import RunOriginDTO, AssessmentJobDTO, RunStatusDTO, StepFunctionStepDTO, RunTypeDTO
from common.api.dtos.cloud_provider_dto import CloudProviderDTO
from common.api.dtos.policy_dto import PolicyDTO, RuleEnforcementModeDTO
from common.api.dtos.rule_result_dto import RuleResultDTO, RuleResultStatusDTO
from common.api.dtos.supported_services_response_dto import SupportedProviderServicesResponseDTO
from common.base_rule_metadata_store import BaseRuleMetadataStore
from common.input_validator import InputValidator
from common.utils import file_utils


@dataclass
class GenerateFilteredPlanCommandParameters(CommandParameters):
    directory: str = None
    tf_plan: str = None
    output_file: str = None
    api_key: str = None
    notty: bool = None
    cloud_provider: Optional[CloudProviderDTO] = None
    base_dir: str = None


@dataclass
class RunCommandParameters(CommandParameters):
    api_key: str = None
    directory: str = None
    tf_plan: str = None
    output_format: str = None
    cloud_account_id: str = None
    cloud_account_name: str = None
    output_file: str = None
    build_link: str = None
    execution_source_identifier: str = None
    filtered_plan: str = None
    auto_approve: bool = None
    no_cloud_account: bool = None
    policy_id: str = None
    refresh_cloud_account_snapshot: bool = None
    junit_package_name_prefix: str = None
    verbose: bool = None
    notty: bool = None
    custom_rules: str = None
    drift_track: bool = None
    cloud_provider: Optional[CloudProviderDTO] = None
    base_dir: str = None


class EvaluationRunCommandService(CommandService):
    def __init__(self, cloudrail_service: CloudrailCliService,
                 terraform_environment_service: TerraformContextService,
                 command_parameters: CommandParameters, command_name: str):
        self.is_tty = command_parameters.origin != RunOriginDTO.CI and not command_parameters.notty and sys.stdout.isatty()
        super().__init__(cloudrail_service, command_parameters, SpinnerWrapper(show_spinner=self.is_tty), self.is_tty, command_name)
        self.terraform_environment_service = terraform_environment_service

    ASSESSMENT_TIMEOUT_SECONDS: int = 600

    def run(self):
        if self.command_parameters.api_key:
            self.cloudrail_service.api_key = self.command_parameters.api_key
        account_config = self._get_account_config()
        self._validate_command_parameters(account_config)
        self._show_origin_warning_message(self.command_parameters.origin)
        account_policies = self._get_account_policies(account_config)
        self._enforce_verbose(account_config, account_policies)
        custom_rules = self.get_custom_rules()
        self.spinner.start('Preparing a filtered Terraform plan locally before uploading to Cloudrail Service...')
        customer_id = self.call_service(self.cloudrail_service.get_my_customer_data, (), ExitCode.BACKEND_ERROR).id
        drift_track = self.command_parameters.drift_track
        job_id = None
        if not self.command_parameters.filtered_plan:
            filtered_plan, checkov_result = self._create_filtered_plan(
                customer_id=customer_id,
                base_dir=self.command_parameters.base_dir,
                cloud_provider=(account_config and account_config.cloud_provider) or self.command_parameters.cloud_provider,
                job_id=job_id,
                submit_failure=False)
            assessment_job: AssessmentJobDTO = self.call_service(self.cloudrail_service.start_assessment_job,
                                                                 (account_config,
                                                                  RunOriginDTO(self.command_parameters.origin),
                                                                  self.command_parameters.build_link,
                                                                  self.command_parameters.execution_source_identifier,
                                                                  self.command_parameters.refresh_cloud_account_snapshot,
                                                                  self.command_parameters.policy_id),
                                                                 ExitCode.BACKEND_ERROR,
                                                                 simple_message=True)
            job_id = assessment_job.id
            self._submit_filtered_plan(filtered_plan, checkov_result, custom_rules, job_id, drift_track)
        else:
            assessment_job: AssessmentJobDTO = self.call_service(self.cloudrail_service.start_assessment_job,
                                                                 (account_config,
                                                                  RunOriginDTO(self.command_parameters.origin),
                                                                  self.command_parameters.build_link,
                                                                  self.command_parameters.execution_source_identifier,
                                                                  self.command_parameters.refresh_cloud_account_snapshot,
                                                                  self.command_parameters.policy_id),
                                                                 ExitCode.BACKEND_ERROR,
                                                                 simple_message=True)
            job_id = assessment_job.id
            self._submit_existing_filtered_plan(custom_rules, job_id, drift_track)
        self.spinner.start('Your job id is: {0}'.format(job_id))
        self._show_account_collect_message(self.command_parameters.refresh_cloud_account_snapshot, assessment_job, account_config)
        assessment_job = self._wait_for_assessment_job_to_complete(assessment_job, time() + self.ASSESSMENT_TIMEOUT_SECONDS)
        if assessment_job.run_status == RunStatusDTO.SUCCESS:
            self._return_assessment_results(assessment_job, account_policies)
        else:
            self.spinner.fail()
            echo_error(generate_failure_message(assessment_job.last_step, assessment_job.error_message, job_id, account_config))
            self._exit_on_failure(self._process_failure_to_exit_code(assessment_job), job_id)

    def generate_filtered_plan(self):
        """
        Send Terraform out file to Cloudrail service for evaluation. We are getting back
        job_id and checking every X sec if the evaluation is done, once the evaluati
        """
        self.command_parameters.origin = validate_origin(self.command_parameters.origin)
        self.command_parameters.tf_plan, self.command_parameters.directory, unused_filtered_plan = validate_input_paths(
            self.command_parameters.tf_plan,
            self.command_parameters.directory,
            None,
            self.is_tty)

        if self.command_parameters.api_key:
            self.cloudrail_service.api_key = self.command_parameters.api_key

        self.spinner.start('Starting...')
        customer_id = self.call_service(self.cloudrail_service.get_my_customer_data, (), ExitCode.BACKEND_ERROR).id
        filtered_plan, _ = self._create_filtered_plan(customer_id=customer_id,
                                                      cloud_provider=self.command_parameters.cloud_provider,
                                                      base_dir=self.command_parameters.base_dir)
        if self.command_parameters.output_file:
            self._save_result_to_file(filtered_plan, self.command_parameters.output_file)
            self.spinner.succeed()
        else:
            click.echo(filtered_plan)
            exit_with_code(ExitCode.OK)

    @staticmethod
    def _save_result_to_file(result: str, output_file: str) -> None:
        try:
            full_path = os.path.join(os.getcwd(), output_file)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            click.echo(f'Saving results to: {output_file}')
            with open(full_path, 'w') as writer:
                writer.write(result)
        except Exception:
            logging.exception('could not write result to file')
            click.echo('failed to write result to file. check folder permission and access.')
            exit_with_code(ExitCode.INVALID_INPUT)

    @staticmethod
    def _process_failure_to_exit_code(assessment_job: AssessmentJobDTO):
        if assessment_job.last_step == StepFunctionStepDTO.PROCESS_BUILDING_ENV_CONTEXT \
                and assessment_job.error_message:
            return ExitCode.CONTEXT_ERROR
        if assessment_job.last_step == StepFunctionStepDTO.RUN_CUSTOM_RULES:
            return ExitCode.INVALID_INPUT
        return ExitCode.BACKEND_ERROR

    @staticmethod
    def _show_origin_warning_message(origin: RunOriginDTO) -> None:
        if origin == RunOriginDTO.CI:
            return
        upper_os_env = {k.upper(): v for k, v in os.environ.items()}
        show_warning = False
        if upper_os_env.get('CI', '').lower() == 'true':
            show_warning = True
        known_keys = {'JOB_NAME', 'BUILD_NUMBER', 'CIRCLECI', 'TRAVIS', 'CI_JOB_NAME', 'CODEBUILD_BUILD_ID'}
        show_warning = show_warning or any(upper_os_env.get(known_key) for known_key in known_keys)
        if show_warning:
            click.echo("NOTE: You are running Cloudrail under CI but without the '--origin' parameter."
                       "\nIt is best to provide that parameter to improve reporting within the Cloudrail Web User Interface.")

    def _show_account_collect_message(self, refresh_cloud_account_snapshot: bool,
                                      assessment_job: AssessmentJobDTO,
                                      account_config: Optional[AccountConfigDTO]):
        if not account_config:
            return
        if refresh_cloud_account_snapshot:
            self.spinner.start('Cloudrail Service is refreshing its cached snapshot of cloud account {}, '
                               'this may take a few minutes...'.format(account_config.cloud_account_id))
        elif assessment_job.run_type == RunTypeDTO.COLLECT_PROCESS_TEST:
            account_status = account_config.status
            if account_status == AccountStatusDTO.INITIAL_ENVIRONMENT_MAPPING:
                self.spinner.start('Cloudrail is still collecting the first snapshot of your cloud account. Please wait. '
                                   'This will not be needed in future runs as a cache version is maintained and refreshed every 1 hour...')
            else:
                self.spinner.start('A recent attempt to collect a snapshot of your cloud account failed. '
                                   'Therefore, Cloudrail is now attempting to collect a fresh snapshot of your cloud account. Please wait. '
                                   'Normally, this is not needed, as a cache version is maintained and refreshed every 1 hour...')
        else:
            self.spinner.start('Cloudrail Service accessing the latest cached snapshot of cloud account {}. '
                               'Timestamp: {}...'.format(account_config.cloud_account_id, account_config.last_collected_at))
        self.spinner.succeed()

    @staticmethod
    def _show_available_policies_message(policies: List[PolicyDTO]) -> str:
        policy_dict = [{'id': policy.id, 'name': policy.name} for policy in policies
                       if policy.active]
        if policy_dict:
            policy_table = tabulate(policy_dict, headers='keys', tablefmt='plain')
            return f'Currently available policies are:' \
                   f'\n{policy_table}' \
                   f'\n\nPlease use the id of the policy.'
        else:
            return 'There are no policies defined and enabled. ' \
                   '\nYou may choose to continue to run without a policy-id and all rules will be evaluated at the Advise level (generating ' \
                   'warnings). '

    def _get_account_config(self) -> Optional[AccountConfigDTO]:
        if self.command_parameters.no_cloud_account:
            return None
        cloud_account_id = self.command_parameters.cloud_account_id or ''
        cloud_account_name = self.command_parameters.cloud_account_name or ''
        account_configs = self.call_service(self.cloudrail_service.list_cloud_accounts, (), ExitCode.BACKEND_ERROR)

        if len(account_configs) == 0:
            self.command_parameters.no_cloud_account = True
            return None
        if len(account_configs) > 1 and not cloud_account_id and not cloud_account_name:
            echo_error('You have added several cloud accounts to Cloudrail. Please provide “--cloud-account-id” with the cloud account’s ID.')
            exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)
        if len(account_configs) == 1 and not cloud_account_id and not cloud_account_name:
            return account_configs[0]
        for account_config in account_configs:
            if account_config.cloud_account_id == cloud_account_id.strip() or account_config.name == cloud_account_name.strip():
                return account_config
        echo_error('The cloud account ID you entered is not recognized.'
                   '\nPlease check it is valid, and if so, add it via the "cloud-account add" command.')
        return exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)

    def _get_account_policies(self, account_config: Optional[AccountConfigDTO]) -> List[PolicyDTO]:
        if not account_config:
            return []
        return self.call_service(self.cloudrail_service.list_policies, ([account_config.id],), ExitCode.BACKEND_ERROR)

    def _create_filtered_plan(self,
                              customer_id: str,
                              cloud_provider: CloudProviderDTO,
                              base_dir: str,
                              job_id: str = None,
                              submit_failure: bool = False):
        self.spinner.start('Re-running your Terraform plan through a customized \'terraform plan\' to generate needed context data...')
        service_result = self.terraform_environment_service.convert_plan_to_json(self.command_parameters.tf_plan,
                                                                                 self.command_parameters.directory)
        if not service_result.success:
            if submit_failure:
                self.cloudrail_service.submit_failure(service_result.error, job_id)
            self.spinner.fail()
            echo_error(generate_convert_terraform_plan_to_json_failure_message(service_result.error, job_id))
            self._exit_on_failure(ExitCode.CLI_ERROR, job_id)
        self.spinner.start('Filtering and processing Terraform data...')
        supported_services_result: SupportedProviderServicesResponseDTO = SupportedProviderServicesResponseDTO(dict())
        cloud_provider = self._calculate_cloud_provider(cloud_provider, service_result.result)
        if cloud_provider == CloudProviderDTO.AMAZON_WEB_SERVICES:
            supported_services_result = self.call_service(self.cloudrail_service.list_aws_supported_services, (), ExitCode.BACKEND_ERROR)
        elif cloud_provider == CloudProviderDTO.AZURE:
            supported_services_result = self.call_service(self.cloudrail_service.list_azure_supported_services, (), ExitCode.BACKEND_ERROR)

        supported_checkov_services_result = self.call_service(self.cloudrail_service.list_checkov_supported_services, (cloud_provider,),
                                                              ExitCode.BACKEND_ERROR)

        supported_checkov_services = supported_checkov_services_result.supported_checkov_services
        checkov_results = self.terraform_environment_service.run_checkov_checks(self.command_parameters.directory,
                                                                                supported_checkov_services,
                                                                                base_dir)

        if not checkov_results.success:
            echo_error(checkov_results.error)
            self._exit_on_failure(ExitCode.BACKEND_ERROR, job_id)

        service_result = self.terraform_environment_service.process_json_result(service_result.result,
                                                                                supported_services_result.supported_services,
                                                                                checkov_results.result,
                                                                                customer_id,
                                                                                ExternalApiClient.get_cli_handshake_version(),
                                                                                base_dir,
                                                                                cloud_provider)

        if not service_result.success:
            if submit_failure:
                self.cloudrail_service.submit_failure(service_result.error, job_id)
            self.spinner.fail()
            echo_error(generate_process_plan_json_failure_message(service_result.error, job_id))
            self._exit_on_failure(ExitCode.CLI_ERROR, job_id)

        self.spinner.start('Obfuscating IP addresses...')
        self.spinner.succeed()
        return service_result.result, checkov_results.result

    def _submit_filtered_plan(self, filtered_plan, checkov_result, custom_rules, job_id, drift_track):
        if not self.command_parameters.auto_approve:
            if not self.is_tty:
                echo_error('You have chosen to do a full run without interactive login. '
                           'This means Cloudrail CLI cannot show you the filtered plan prior to uploading to the Cloudrail Service. '
                           'In such a case you can either:'
                           '\n1. Execute \'cloudrail generate-filtered-plan\' '
                           'first, then provide the file to \'cloudrail run --filtered-plan\'.'
                           '\n2. Re-run \'cloudrail run\' with \'--auto-approve\', '
                           'indicating you are approving the upload of the filtered plan to Cloudrail Service.')
                exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)
            click.echo(highlight(filtered_plan, JsonLexer(), Terminal256Formatter(style=MonokaiStyle)))
            if checkov_result:
                click.echo('For some non-context-aware rules, '
                           'Cloudrail utilized the Checkov engine and found a few violations.'
                           '\nSuch violations will be marked with the \'CKV_*\' rule ID.\n')
            approved = click.confirm('OK to upload this Terraform data to Cloudrail'
                                     ' (use \'--auto-approve\' to skip this in the future)?', default=True)
            if not approved:
                self.cloudrail_service.submit_failure('terraform data not approved for upload', job_id)
                echo_error('Upload not approved. Aborting.')
                exit_with_code(ExitCode.USER_TERMINATION, self.command_parameters.no_fail_on_service_error)

        self.spinner.start('Submitting Terraform data to the Cloudrail Service...')
        self.call_service(self.cloudrail_service.submit_filtered_plan, (filtered_plan, job_id, custom_rules, drift_track),
                          ExitCode.BACKEND_ERROR, simple_message=True)

    def _submit_existing_filtered_plan(self, custom_rules, job_id: str, drift_track: bool):
        service_result = self.terraform_environment_service.read_terraform_output_file(self.command_parameters.filtered_plan)
        if not service_result.success:
            echo_error(generate_simple_message('Error while reading json file. This is probably due to an '
                                               'outdated Terraform show output generated by Cloudrail CLI container.'
                                               '\nPlease pull the latest version of this container and use \'generated-filtered-plan\' '
                                               'to regenerate the file.', job_id))
            exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)
        self.spinner.start('Submitting Terraform data to the Cloudrail Service...')
        self.call_service(self.cloudrail_service.submit_filtered_plan, (service_result.result, job_id, custom_rules, drift_track),
                          ExitCode.BACKEND_ERROR, simple_message=True)

    def _wait_for_assessment_job_to_complete(self, assessment_job: AssessmentJobDTO, timeout):
        run_status = RunStatusDTO.RUNNING
        last_step = None
        while run_status == RunStatusDTO.RUNNING and timeout >= time():
            sleep(1)
            assessment_job = self.call_service(self.cloudrail_service.get_assessment_job, (assessment_job.id,), ExitCode.BACKEND_ERROR,
                                               'Error while waiting for analysis', True)
            messages = self._get_progress_messages(last_step, assessment_job.last_step)
            for msg in messages:
                self.spinner.start(msg)
                sleep(0.5)
            last_step = assessment_job.last_step
            run_status = assessment_job.run_status
            if timeout < time():
                echo_error(generate_simple_message('Timeout while waiting for assessment to be completed. Please try again.'
                                                   '\nIf the issue persists, please contact us using the details provided below.',
                                                   assessment_job.id))
                exit_with_code(ExitCode.TIMEOUT, self.command_parameters.no_fail_on_service_error)
        return assessment_job

    def _return_assessment_results(self, assessment_job: AssessmentJobDTO, account_policies: List[PolicyDTO]):
        self.spinner.start('Assessment complete, fetching results...')
        rule_results = self.call_service(self.cloudrail_service.get_assessment_results, (assessment_job.id,), ExitCode.BACKEND_ERROR,
                                         'Error while fetching rule results', True)
        self.spinner.succeed()
        stylize = self.command_parameters.output_file == ''
        censored_api_key = 'XXXXX' + self.cloudrail_service.api_key[-4:]
        formatter = self._get_formatter(self.command_parameters.output_format, censored_api_key, self.command_parameters.directory,
                                        self.command_parameters.tf_plan,
                                        self.command_parameters.junit_package_name_prefix, stylize, self.command_parameters.verbose)
        format_result, notices = formatter(rule_results, assessment_job, account_policies)
        if self.command_parameters.output_file:
            self._save_result_to_file(format_result, self.command_parameters.output_file)
        else:
            click.echo(format_result)
        if notices:
            click.echo(notices)
        ui_url = f'{self.cloudrail_service.api_client.get_api_base_url()}/environments/assessments/{assessment_job.id}'.replace('api', 'web')
        click.echo(f'To view this assessment in the Cloudrail Web UI, '
                   f'go to {ui_url}')
        self._send_exit_code(rule_results, self.command_parameters.no_fail_on_service_error)

    @staticmethod
    def _get_formatter(output_format: str, api_key: str, directory: str, plan_path: str, junit_package_name_prefix: str, stylize: bool,
                       verbose: bool):
        if output_format == 'junit':
            click.echo('IMPORTANT: When using the JUnit format output, Cloudrail CLI will only include rules that are set to ‘mandate’. '
                       'If a violation is found with such rules, a test failure will be logged in the JUnit output. '
                       'Rules that are set to ‘advise’ will not be included in the JUnit output, and can be viewed in the Cloudrail web user '
                       'interface.')
            return JunitFormatter(api_key, directory, plan_path, junit_package_name_prefix).format
        if output_format == 'json':
            return JsonFormatter(verbose).format
        if output_format == 'json-gitlab-sast':
            return JsonGitLabSastFormatter(verbose).format
        if output_format == 'sarif':
            return SarifFormatter(verbose).format
        return TextFormatter(stylize, verbose).format

    @staticmethod
    def _send_exit_code(rule_results: List[RuleResultDTO], no_fail_on_service_error):
        for rule_result in rule_results:
            if rule_result.status == RuleResultStatusDTO.FAILED \
                    and rule_result.is_mandate:
                exit_with_code(ExitCode.MANDATORY_RULES_FAILED, no_fail_on_service_error)
        exit_with_code(ExitCode.OK, no_fail_on_service_error)

    def _validate_command_parameters(self, account_config: AccountConfigDTO):
        self._validate_account(account_config)
        self.command_parameters.origin = validate_origin(self.command_parameters.origin, self.command_parameters.no_fail_on_service_error)
        self._validate_build_link(self.command_parameters.build_link, self.command_parameters.origin,
                                  self.command_parameters.no_fail_on_service_error)
        validate_cloud_account_input(self.command_parameters.cloud_account_id, self.command_parameters.cloud_account_name, allow_both_none=True)
        self._validate_policy()
        self.command_parameters.tf_plan, \
        self.command_parameters.directory, \
        self.command_parameters.filtered_plan = \
            validate_input_paths(self.command_parameters.tf_plan,
                                 self.command_parameters.directory,
                                 self.command_parameters.filtered_plan,
                                 self.is_tty)

    def _validate_policy(self):
        if self.command_parameters.policy_id and not self.command_parameters.no_cloud_account:
            echo_error('You have provided --policy-id, but this is currently supported only in conjunction with --no-cloud-account.')
            exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)
        if self.command_parameters.policy_id and self.command_parameters.no_cloud_account:
            policies = self.call_service(self.cloudrail_service.list_policies, (), ExitCode.BACKEND_ERROR)
            selected_policy = next((policy for policy in policies if policy.id == self.command_parameters.policy_id), None)
            if not selected_policy:
                echo_error(f'No policy found by that identifier. '
                           f'{self._show_available_policies_message(policies)}')
                exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)
            if not selected_policy.active:
                echo_error(f'The policy {self.command_parameters.policy_id} is disabled, please use a different one.'
                           f'\n{self._show_available_policies_message(policies)}')
                exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)

    @staticmethod
    def _validate_build_link(build_link: str, origin: RunOriginDTO, no_fail_on_service_error: bool):
        if origin == RunOriginDTO.CI and not build_link:
            echo_error('You\'ve set --origin to \'ci\', please also supply \'--build-link\'.')
            exit_with_code(ExitCode.INVALID_INPUT, no_fail_on_service_error)
        return build_link

    def _validate_account(self, account_config: AccountConfigDTO):
        if account_config is None or account_config.cloud_provider == CloudProviderDTO.AMAZON_WEB_SERVICES:
            account_id_regex = InputValidator.get_aws_account_id_regex()
            if self._is_account_id_valid(account_id_regex):
                echo_error('The AWS Account ID should be 12 digits, without hyphens or other characters. Please try again')
                exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)
        elif account_config.cloud_provider == CloudProviderDTO.AZURE:
            account_id_regex = InputValidator.get_uuid_regex()
            if self._is_account_id_valid(account_id_regex):
                echo_error('The Azure Account ID should be in valid UUID format, Please try again')
                exit_with_code(ExitCode.INVALID_INPUT, self.command_parameters.no_fail_on_service_error)

    def _is_account_id_valid(self, account_id_regex: str) -> bool:
        return account_id_regex and \
               self.command_parameters.cloud_account_id and \
               not re.match(account_id_regex, self.command_parameters.cloud_account_id) is not None

    @staticmethod
    def _get_progress_messages(last_step: StepFunctionStepDTO, current_step: StepFunctionStepDTO = None) -> List[str]:
        messages = {5: 'Building simulated graph model, representing how the cloud account will look like if the plan were to be applied...',
                    6: 'Running context-aware rules...',
                    7: 'Running custom rules...',
                    8: 'Returning results, almost done!'}
        steps: List[StepFunctionStepDTO] = StepFunctionStepDTO.get_steps()
        last_step_index = steps.index(last_step) if last_step else 0
        current_step_index = steps.index(current_step) if current_step else 0
        return [messages.get(i) for i in range(last_step_index + 1, current_step_index + 1) if messages.get(i)]

    # pylint: disable=R1710
    def get_custom_rules(self) -> dict:
        try:
            custom_rules = {'rules': {}, 'rules_metadata': {}}
            metadata_store: BaseRuleMetadataStore = None
            if not self.command_parameters.custom_rules:
                return self.command_parameters.custom_rules
            self.spinner.start('Reading custom rules...')
            for custom_rules_tuple in self.command_parameters.custom_rules:
                if ":" in custom_rules_tuple:
                    custom_rules_args = custom_rules_tuple.split(':')
                    enforcement_mode = self._get_rule_enforcement_mode(custom_rules_args[0])
                    custom_rules_dir = custom_rules_args[1]
                else:
                    enforcement_mode = RuleEnforcementModeDTO.ADVISE
                    custom_rules_dir = custom_rules_tuple
                abs_custom_rules_dir = os.path.abspath(custom_rules_dir.strip())
                if not os.path.isdir(abs_custom_rules_dir):
                    echo_error(f'The path you have provided "{custom_rules_dir}" does not point to a specific folder.'
                               '\nPlease provide the path directly to the custom rules you wish to use Cloudrail with.')
                    exit_with_code(ExitCode.INVALID_INPUT)
                rules_metadata_path = os.path.join(abs_custom_rules_dir, 'rules_metadata.yaml')
                if not os.path.isfile(rules_metadata_path):
                    echo_error(f'The path you have provided "{custom_rules_dir}" does not contain rules_metadata.yaml file.'
                               '\nPlease provide the path directly to the custom rules you wish to use Cloudrail with.')
                    exit_with_code(ExitCode.INVALID_INPUT)
                custom_rules['rules'][enforcement_mode] = custom_rules['rules'].get(enforcement_mode, {})
                found_rules = []
                files_in_dir = file_utils.get_all_files(abs_custom_rules_dir, {'venv'})
                for full_file_name in files_in_dir:
                    if full_file_name.endswith('.py'):
                        rule_id = self.get_rule_id(full_file_name)
                        if rule_id:
                            content = file_utils.read_all_text(full_file_name)
                            zipped_content = base64.b64encode(zlib.compress(content.encode())).decode()
                            custom_rules['rules'][enforcement_mode][full_file_name] = zipped_content
                            found_rules.append(rule_id)

                rule_metadata_raw_data = file_utils.file_to_yaml(rules_metadata_path)
                custom_rule_metadata_store = BaseRuleMetadataStore(rule_metadata_raw_data)
                if metadata_store:
                    metadata_store.merge(custom_rule_metadata_store)
                else:
                    metadata_store = custom_rule_metadata_store
                rule_ids_with_metadata = custom_rule_metadata_store.list_rules_ids()
                rules_without_metadata = set(found_rules) - set(rule_ids_with_metadata)
                if rules_without_metadata:
                    raise Exception(f'Invalid custom rules without metadata: {rules_without_metadata}')
                rules_without_logic = set(rule_ids_with_metadata) - set(found_rules)
                if rules_without_logic:
                    raise Exception(f'Invalid custom rules without logic: {rules_without_logic}')
            custom_rules['rules_metadata'] = metadata_store.raw_metadata
            return custom_rules
        except Exception as ex:
            echo_error(str(ex))
            exit_with_code(ExitCode.INVALID_INPUT)

    @staticmethod
    def get_rule_id(full_file_name: str) -> Optional[str]:
        module_dir = os.path.dirname(full_file_name)
        module_name = os.path.splitext(os.path.basename(full_file_name))[0]
        sys.path.insert(0, module_dir)
        module = __import__(module_name)
        importlib.reload(module)
        classes = inspect.getmembers(module, inspect.isclass)
        for _, class_name in classes:
            try:
                if issubclass(class_name, BaseRule) and class_name().get_id():
                    return class_name().get_id()
            except Exception:
                pass
        return None

    def _calculate_cloud_provider(self, cloud_provider: Optional[CloudProviderDTO], plan_json_path: str) -> CloudProviderDTO:
        if cloud_provider:
            return cloud_provider
        dic = file_utils.file_to_yaml(plan_json_path)
        aws_resource_found = False
        azure_resource_found = False
        for resource in dic.get('resource_changes', []):
            if resource['type'].startswith('aws_'):
                aws_resource_found = True
            if resource['type'].startswith('azurerm_'):
                azure_resource_found = True
            if aws_resource_found and azure_resource_found:
                self.spinner.fail()
                echo_error('Cloudrail supports running an analysis for one cloud provider only. Please pass --cloud-provider.')
                exit_with_code(ExitCode.INVALID_INPUT)
        if not aws_resource_found and not azure_resource_found:
            self.spinner.fail()
            echo_error('Cloudrail currently supports the following cloud providers: aws, azure. '
                       'The code provided does not seem to be using any of the supported providers.')
            exit_with_code(ExitCode.INVALID_INPUT)
        if aws_resource_found:
            return CloudProviderDTO.AMAZON_WEB_SERVICES
        else:
            return CloudProviderDTO.AZURE

    def _enforce_verbose(self, account_config: Optional[AccountConfigDTO], account_policies: List[PolicyDTO]):
        if not account_config:
            self.command_parameters.verbose = True
            self.spinner.start("No cloud account is used in this analysis, showing all FAILUREs and WARNINGs.")
        elif not account_policies:
            self.command_parameters.verbose = True
            self.spinner.start("The cloud account used in this analysis doesn't have a policy set, showing all FAILUREs and WARNINGs.")

    @staticmethod
    def _get_rule_enforcement_mode(value) -> RuleEnforcementModeDTO:
        optional_values = [RuleEnforcementModeDTO.ADVISE.value,
                           RuleEnforcementModeDTO.MANDATE_ALL_RESOURCES.value,
                           RuleEnforcementModeDTO.MANDATE_NEW_RESOURCES.value]
        if value.lower() not in optional_values:
            echo_error(f'Unsupported enforcement mode \'{value}\'.\nAvailable options are {optional_values}')
            exit_with_code(ExitCode.INVALID_INPUT)
        return RuleEnforcementModeDTO(value.lower())
