import json
import logging
import os
from dataclasses import dataclass
from enum import Enum
from http import HTTPStatus
from typing import Union, List, Optional

from cloudrail.cli.api_client.contract.cloudrail_api_response import BaseCloudrailResponse, CloudrailErrorResponse, \
    CloudrailSuccessJsonResponse, CloudrailSuccessDataResponse, CloudrailUnauthorizedResponse
from cloudrail.cli.api_client.external_api_client import ExternalApiClient
from cloudrail.cli.cli_configuration import CliConfiguration, CliConfigurationKey
from common.api.dtos.account_config_dto import AccountConfigDTO, AccountConfigAddDTO, AccountConfigUpdateDTO, CloudProviderDTO, AzureCredentialsDTO
from common.api.dtos.assessment_job_dto import AssessmentJobDTO, RunOriginDTO
from common.api.dtos.assessment_result_dto import AssessmentResultDTO, AssessmentResultTypeDTO
from common.api.dtos.connection_test_dto import ConnectionTestDTO, ConnectivityTestRequestDTO
from common.api.dtos.customer_dto import CustomerDTO
from common.api.dtos.drift_detection_dto import DriftDetectionJobDTO
from common.api.dtos.environment_context_dto import EnvironmentContextResultDTO
from common.api.dtos.external_integration_dto import AddUpdateExternalIntegrationDTO, ExternalIntegrationDTO
from common.api.dtos.filter_block_dto import FilterBlockDTO
from common.api.dtos.pagination_result_dto import PaginationResultDTO
from common.api.dtos.policy_dto import PolicyDTO, PolicyUpdateDTO, PolicyRuleDTO, PolicyRuleUpdateDTO, PolicyAddDTO, PolicyRuleBulkAddDataDTO, \
    RuleEnforcementModeDTO
from common.api.dtos.rule_info_dto \
    import RuleInfoDTO, RuleUpdateDTO, RuleBulkUpdateDTO, RuleSeverityDTO, RuleTypeDTO, SecurityLayerDTO, ResourceTypeDTO
from common.api.dtos.rule_result_dto import RuleResultDTO
from common.api.dtos.rule_task_dto import RuleTaskDTO
from common.api.dtos.supported_services_response_dto import SupportedProviderServicesResponseDTO, SupportedCheckovServicesResponseDTO
from common.api.dtos.user_dto import UserDTO, UserWithTokenDTO, UserLoginDTO, UserRegisterDTO, UserUnregisterDTO, ApiKeyDTO, UserUpdateDTO, \
    UserChangePasswordDTO, UserInviteDTO, UserInvitationSummaryDTO, UserRegisterWithInvitationDTO, UserResetPasswordRequestSummaryDTO, \
    UserResetPasswordDTO, UserResetPasswordRequestDTO, UserConfirmationDTO


class ApiStatus(str, Enum):
    SUCCESS = 'success'
    FAILURE = 'failure'
    UNAUTHORIZED = 'unauthorzied'


@dataclass
class APIResult:
    status: ApiStatus
    response: Union[str, dict]

    @property
    def success(self):
        return self.status == ApiStatus.SUCCESS


class CloudrailApiClient(ExternalApiClient):
    LOGIN_PATH: str = '/users/login'
    LOGOUT_PATH: str = '/users/logout'
    USER_ID_PATH: str = '/users/{0}'
    USER_ID_CHANGE_PASSWORD_PATH: str = '/users/{0}/password/change'
    USER_RESET_PASSWORD_REQUEST_PATH: str = '/users/password/reset/request'
    USER_RESET_PASSWORD_CONFIRM_PATH: str = '/users/password/reset/confirm'
    USERS: str = '/users/'
    USER_GET_MY_PROFILE_PATH: str = '/users/me'
    USER_INVITE_PATH: str = '/users/invite'
    REGISTER_PATH: str = '/users/register'
    COMPLETE_REGISTRATION_PATH: str = '/users/complete_registration'
    USER_CONFIRM_REGISTRATION_PATH: str = '/users/confirmation'
    API_KEY_PATH: str = '/users/{0}/apikey'
    UN_REGISTER_PATH: str = '/users/unregister'
    ACCOUNTS_PATH: str = '/accounts?query={0}&sort_by={1}&sort_direction={2}'
    ADD_ACCOUNTS_PATH: str = '/accounts?verify={0}&collect={1}'
    ACCOUNT_ID_PATH: str = '/accounts/{0}'
    ACCOUNT_CONNECTIVITY_TEST: str = '/accounts/connectivity/test'
    POLICY_ID_PATH: str = '/policies/{0}'
    ADD_POLICY_PATH: str = '/policies'
    LIST_POLICIES_PATH: str = '/policies?{0}&query={1}&sort_by={2}&sort_direction={3}'
    ADD_POLICIES_ACCOUNTS: str = '/policies/{0}/accounts'
    DELETE_POLICIES_ACCOUNT: str = '/policies/{0}/accounts/{1}'
    POLICY_RULES_PATH: str = '/policies/{0}/rules'
    ADD_BULK_POLICIES_RULES: str = '/policies/rules'
    POLICIES_RULES_ID: str = '/policies/{0}/rules/{1}'
    START_ASSESSMENT_JOB: str = '/assessments/jobs?run_collect={0}&account_config_id={1}&origin={2}&build_link={3}&execution_source_identifier={' \
                                '4}&skip_collect={5}&policy_id={6}'
    ASSESSMENT_JOB_SUBMIT_FILTERED_PLAN = '/assessments/jobs/{0}/filtered_plan'
    ASSESSMENT_JOB: str = '/assessments/jobs/{0}'
    UPLOAD_LOG: str = '/logs/cli?job_id={0}&command={1}'
    CUSTOMERS_PATH: str = '/customers/{0}'
    CUSTOMERS_API_KEY_PATH: str = '/customers/me/apikey'
    CUSTOMERS_ME_PATH: str = '/customers/me'
    CUSTOMERS_TERRAFORM_TEMPLATE_PATH: str = '/customers/{0}/terraform_template'
    LIST_RULES_PATH: str = '/rules?query={0}' \
                           '&policy_id={1}' \
                           '&has_policy_association={2}' \
                           '&severity={3}' \
                           '&cloud_provider={4}' \
                           '&rule_type={5}' \
                           '&security_layer={6}' \
                           '&resource_type={7}' \
                           '&active={8}'
    RULE_ID_PATH: str = '/rules/{0}'
    UPDATE_RULES_PATH: str = '/rules'
    RULE_FILTERS_PATH: str = '/rules/filters'
    ASSESSMENT_FILTERS_PATH: str = '/assessments/results/filters'
    RULE_RESULTS_PATH: str = '/rules/results?assessment_id={0}' \
                             '&result_status={1}' \
                             '&enforcement_mode={2}' \
                             '&policy_id={3}' \
                             '&severity={4}' \
                             '&rule_type={5}' \
                             '&security_layer={6}' \
                             '&resource_type={7}' \
                             '&query={8}' \
                             '&start_date={9}' \
                             '&end_date={10}'
    RULE_RESULT_FILTERS_PATH: str = '/rules/results/filters'
    ASSESSMENTS_RESULTS_PATH: str = '/assessments/results?query={0}' \
                                    '&origin={1}' \
                                    '&no_cloud_account={2}' \
                                    '&cloud_provider={3}' \
                                    '&result_status={4}' \
                                    '&cloud_account_id={5}' \
                                    '&start_date={6}' \
                                    '&end_date={7}&page={8}' \
                                    '&items_per_page={9}' \
                                    '&sort_direction={10}' \
                                    '&sort_by={11}'
    ASSESSMENTS_RESULTS_ID_PATH: str = '/assessments/results/{0}'
    RULES_TASKS_PATH: str = '/task_center/rules/tasks?query={0}'
    RULES_TASK_RESULTS_PATH: str = '/task_center/rules/{0}/results'
    VERSION_PATH: str = '/version'
    AWS_SUPPORTED_SERVICES: str = '/supported_services/aws'
    AZURE_SUPPORTED_SERVICES: str = '/supported_services/azure'
    CHECKOV_SUPPORTED_SERVICES: str = '/supported_services/checkov?cloud_provider={0}'
    FEATURE_FLAGS_PATH: str = '/feature_flags?{}'
    DRIFT_DETECTION_JOBS_LATEST_LIST: str = '/drift_detection/jobs/latest'
    DRIFT_DETECTION_RESULTS_GET: str = '/drift_detection/results/{0}'
    INTEGRATION_PATH: str = '/settings/integrations/{0}'
    INTEGRATIONS_PATH: str = '/settings/integrations'

    def __init__(self, service_endpoint: str = None):
        endpoint = service_endpoint \
                   or os.getenv('CLOUDRAIL_API_GATEWAY') \
                   or CliConfiguration().get(CliConfigurationKey.ENDPOINT) \
                   or 'https://api.cloudrail.app'
        ExternalApiClient.__init__(self, endpoint)

    def login(self, email: str, password: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.LOGIN_PATH,
                                                          UserLoginDTO(email=email,
                                                                       password=password).to_dict()),
                                        custom_log_message='login')
        return self._parse_api_result(api_result, UserWithTokenDTO.from_dict)

    def logout(self, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.LOGOUT_PATH),
                                        custom_log_message='logout',
                                        access_token=access_token)
        return self._parse_api_result(api_result)

    def get_my_profile(self, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.USER_GET_MY_PROFILE_PATH),
                                        custom_log_message='get my profile',
                                        access_token=access_token)
        return self._parse_api_result(api_result, UserDTO.from_dict)

    def list_users(self, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.USERS),
                                        custom_log_message='list users',
                                        access_token=access_token)
        return self._parse_api_result(api_result, lambda x: [UserDTO.from_dict(user) for user in x])

    def update_user(self, email: str, user_update_dto: UserUpdateDTO, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.patch(self.USER_ID_PATH.format(email), user_update_dto.to_dict()),
                                        custom_log_message='update user',
                                        access_token=access_token)
        return self._parse_api_result(api_result, UserDTO.from_dict)

    def change_password(self, email: str, user_update_dto: UserChangePasswordDTO, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.patch(self.USER_ID_CHANGE_PASSWORD_PATH.format(email), user_update_dto.to_dict()),
                                        custom_log_message='change user password',
                                        access_token=access_token)
        return self._parse_api_result(api_result)

    def request_reset_password(self, reset_password_request_dto: UserResetPasswordRequestDTO) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.USER_RESET_PASSWORD_REQUEST_PATH,
                                                          reset_password_request_dto.to_dict()),
                                        custom_log_message='reset password request')
        return self._parse_api_result(api_result, UserResetPasswordRequestSummaryDTO.from_dict)

    def confirm_reset_password(self, reset_password_dto: UserResetPasswordDTO) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.USER_RESET_PASSWORD_CONFIRM_PATH,
                                                          reset_password_dto.to_dict()),
                                        custom_log_message='reset password confirm')
        return self._parse_api_result(api_result)

    def delete_user(self, email: str, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.delete(self.USER_ID_PATH.format(email)),
                                        custom_log_message='delete user',
                                        access_token=access_token)
        return self._parse_api_result(api_result)

    def get_user(self, email: str, access_token: str = None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.USER_ID_PATH.format(email)),
                                        custom_log_message='get user',
                                        access_token=access_token)
        return self._parse_api_result(api_result, UserDTO.from_dict)

    def register(self, email: str, password: str, first_name: str, last_name: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.REGISTER_PATH,
                                                          UserRegisterDTO(email=email,
                                                                          password=password,
                                                                          first_name=first_name,
                                                                          last_name=last_name).to_dict()),
                                        custom_log_message='register')
        return self._parse_api_result(api_result, UserDTO.from_dict)

    def invite_user(self, user_invite_dto: List[UserInviteDTO], access_token: str):
        api_result = self._send_request(lambda: self.post(self.USER_INVITE_PATH,
                                                          data=UserInviteDTO.schema().dumps(user_invite_dto, many=True)),
                                        custom_log_message='invite user',
                                        access_token=access_token)
        return self._parse_api_result(api_result, lambda x: [UserInvitationSummaryDTO.from_dict(user_invite_summary)
                                                             for user_invite_summary in x])

    def complete_registration(self, register_with_invitation: UserRegisterWithInvitationDTO):
        api_result = self._send_request(lambda: self.patch(self.COMPLETE_REGISTRATION_PATH,
                                                           register_with_invitation.to_dict()),
                                        custom_log_message='complete user registration')
        return self._parse_api_result(api_result, UserWithTokenDTO.from_dict)

    def confirm_registration(self, email: str, confirmation_code: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.USER_CONFIRM_REGISTRATION_PATH,
                                                          UserConfirmationDTO(email, confirmation_code).to_dict()),
                                        custom_log_message='confirm registration')
        if not api_result.success:
            return CloudrailErrorResponse(message=api_result.response)
        return CloudrailSuccessJsonResponse()

    def generate_api_key(self, email: str, access_token: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.API_KEY_PATH.format(email)),
                                        custom_log_message='generate api key',
                                        access_token=access_token)
        return self._parse_api_result(api_result, ApiKeyDTO.from_dict)

    def get_api_key(self, email: str, access_token: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.API_KEY_PATH.format(email)),
                                        custom_log_message='get api key',
                                        access_token=access_token)

        def create_api_key_result(result):
            if result:
                return ApiKeyDTO.from_dict(result)
            else:
                return None

        return self._parse_api_result(api_result, create_api_key_result)

    def unregister(self, email: str, password: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.post(self.UN_REGISTER_PATH,
                                                          UserUnregisterDTO(email=email, password=password).to_dict()),
                                        custom_log_message='unregister')
        return self._parse_api_result(api_result)

    def list_accounts(self, api_key: str,
                      query: Optional[str] = None,
                      sort_by: Optional[str] = None,
                      sort_direction: Optional[str] = None) -> BaseCloudrailResponse:

        api_result = self._send_request(lambda: self.get(self.ACCOUNTS_PATH.format(query or '',
                                                                                   sort_by or '',
                                                                                   sort_direction or '')), api_key, 'list accounts')
        return self._parse_api_result(api_result, lambda x: [AccountConfigDTO.from_dict(account) for account in x])

    def update_account(self, api_key: str, account_config_id: str, account_name: str) -> BaseCloudrailResponse:
        payload = AccountConfigUpdateDTO(name=account_name).to_dict()
        api_result = self._send_request(lambda: self.patch(self.ACCOUNT_ID_PATH.format(account_config_id), payload), api_key, 'update cloud account')
        return self._parse_api_result(api_result, AccountConfigDTO.from_dict)

    def get_account(self, api_key: str, account_config_id: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.ACCOUNT_ID_PATH.format(account_config_id)), api_key, 'get cloud account')
        return self._parse_api_result(api_result, AccountConfigDTO.from_dict)

    def list_policies(self,
                      api_key: str,
                      account_config_ids: List[str] = None,
                      query: str = '',
                      sort_by: str = '',
                      sort_direction: str = '') -> BaseCloudrailResponse:
        param = self._get_multiple_param_query('account_config_id', account_config_ids)
        api_result = self._send_request(lambda: self.get(self.LIST_POLICIES_PATH.format(param,
                                                                                        query,
                                                                                        sort_by,
                                                                                        sort_direction)), api_key, 'list policies')
        return self._parse_api_result(api_result, lambda x: [PolicyDTO.from_dict(policy) for policy in x])

    def get_policy(self, api_key: str, policy_id: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.POLICY_ID_PATH.format(policy_id)), api_key, 'get policy')
        return self._parse_api_result(api_result, PolicyDTO.from_dict)

    def update_policy(self, api_key: str, policy_id: str, policy_update_dto: PolicyUpdateDTO):
        api_result = self._send_request(lambda: self.patch(self.POLICY_ID_PATH.format(policy_id), policy_update_dto.to_dict()), api_key,
                                        'update policy')
        return self._parse_api_result(api_result, PolicyDTO.from_dict)

    def add_policy_account_configs(self, api_key: str, policy_id: str, account_config_ids: List[str]):
        api_result = self._send_request(lambda: self.patch(self.ADD_POLICIES_ACCOUNTS.format(policy_id), data=json.dumps(account_config_ids)),
                                        api_key, 'add policy account')
        return self._parse_api_result(api_result, PolicyDTO.from_dict)

    def delete_policy_account_config(self, api_key: str, policy_id: str, account_config_id: str):
        api_result = self._send_request(lambda: self.delete(self.DELETE_POLICIES_ACCOUNT.format(policy_id, account_config_id)),
                                        api_key,
                                        'remove policy_account_config')
        return self._parse_api_result(api_result)

    def add_policy_rules(self, api_key: str, policy_id: str, policy_rules: List[PolicyRuleDTO]):
        policy_rules = PolicyRuleDTO.schema().dumps(policy_rules, many=True)
        api_result = self._send_request(lambda: self.patch(self.POLICY_RULES_PATH.format(policy_id), data=policy_rules), api_key,
                                        'add policy rules')
        return self._parse_api_result(api_result, PolicyDTO.from_dict)

    def add_bulk_policy_rules(self, api_key: str, policy_rules: List[PolicyRuleBulkAddDataDTO]):
        policy_rules = PolicyRuleBulkAddDataDTO.schema().dumps(policy_rules, many=True, default=lambda o: o.__dict__)
        api_result = self._send_request(lambda: self.patch(self.ADD_BULK_POLICIES_RULES, data=policy_rules), api_key,
                                        'add bulk policy rules')
        return self._parse_api_result(api_result, lambda x: [PolicyDTO.from_dict(policy) for policy in x])

    def update_policy_rule(self, api_key: str, policy_id: str, rule_id: str, policy_rule_update: PolicyRuleUpdateDTO):
        api_result = self._send_request(lambda: self.patch(self.POLICIES_RULES_ID.format(policy_id, rule_id), policy_rule_update.to_dict()),
                                        api_key, 'add policy account')
        return self._parse_api_result(api_result, PolicyDTO.from_dict)

    def delete_policy_rule(self, api_key: str, policy_id: str, rule_id: str):
        api_result = self._send_request(lambda: self.delete(self.POLICIES_RULES_ID.format(policy_id, rule_id)),
                                        api_key,
                                        'remove policy rule')
        return self._parse_api_result(api_result)

    def delete_policy_rules(self, api_key: str, policy_id: str, rule_ids: List[str]):
        rule_ids_query = self._get_multiple_param_query('rule_id', rule_ids)
        path = f'{self.POLICY_RULES_PATH.format(policy_id)}?{rule_ids_query}'
        api_result = self._send_request(lambda: self.delete(path),
                                        api_key,
                                        'remove policy rules')
        return self._parse_api_result(api_result)

    def remove_cloud_account(self, api_key: str, cloud_account_id: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.delete(self.ACCOUNT_ID_PATH.format(cloud_account_id)),
                                        api_key,
                                        'remove cloud account')
        return self._parse_api_result(api_result)

    def remove_policy(self, api_key: str, policy_id: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.delete(self.POLICY_ID_PATH.format(policy_id)),
                                        api_key,
                                        'remove policy')
        return self._parse_api_result(api_result)

    def add_cloud_account(self, api_key: str, account_name: str, account_id: str, pull_interval: int, cloud_provider: CloudProviderDTO, verify: bool,
                          collect: bool, client_id: Optional[str] = None, client_secret: Optional[str] = None,
                          tenant_id: Optional[str] = None, disable_collect: bool = False) -> BaseCloudrailResponse:
        payload = AccountConfigAddDTO(
            name=account_name,
            interval_seconds=pull_interval,
            cloud_account_id=account_id,
            cloud_provider=cloud_provider,
            disable_collect=disable_collect)
        if cloud_provider == CloudProviderDTO.AZURE:
            credentials = AzureCredentialsDTO(tenant_id, client_id, client_secret)
            payload.credentials = credentials
        api_result = self._send_request(lambda: self.post(self.ADD_ACCOUNTS_PATH.format(verify, collect), payload.to_dict()), api_key,
                                        'add cloud account')
        return self._parse_api_result(api_result, AccountConfigDTO.from_dict)

    def add_policy(self, api_key: str, policy_dto: PolicyAddDTO) -> BaseCloudrailResponse:
        payload = policy_dto.to_dict()
        api_result = self._send_request(lambda: self.post(self.ADD_POLICY_PATH, payload), api_key, 'add policy')
        return self._parse_api_result(api_result, PolicyDTO.from_dict)

    def start_assessment_job(self,
                             api_key: str,
                             run_collect: bool,
                             account_config_id: Optional[str],
                             origin: RunOriginDTO,
                             build_link: str,
                             execution_source_identifier: str,
                             skip_collect: bool,
                             policy_id: str) -> BaseCloudrailResponse:
        path = self.START_ASSESSMENT_JOB.format(run_collect.__str__().lower(),
                                                account_config_id or '',
                                                origin.value,
                                                build_link or '',
                                                execution_source_identifier or '',
                                                skip_collect.__str__().lower(),
                                                policy_id or '')
        api_result = self._send_request(
            lambda: self.post(path), api_key, 'run')
        return self._parse_api_result(api_result, AssessmentJobDTO.from_dict)

    def submit_filtered_plan(self,
                             api_key: str,
                             job_id: str,
                             show_output: str,
                             custom_rules: dict,
                             drift_track: bool) -> BaseCloudrailResponse:
        try:
            context = json.loads(show_output)
            context['custom_rules'] = custom_rules
            cloud_provider = context['cloud_provider']
            output = json.dumps(context)
        except Exception as ex:
            self.submit_failure(api_key, job_id, str(ex))
            return CloudrailErrorResponse(message="failed to serialize json from Terraform output file")
        data = EnvironmentContextResultDTO(True, output, drift_track=drift_track, cloud_provider=cloud_provider)
        path = self.ASSESSMENT_JOB_SUBMIT_FILTERED_PLAN.format(job_id)
        api_result = self._send_request(
            lambda: self.post(path, data.to_dict()), api_key, 'submit Terraform output')
        return self._parse_api_result(api_result)

    def submit_failure(self,
                       api_key: str,
                       job_id: str,
                       failure: str) -> BaseCloudrailResponse:
        data = EnvironmentContextResultDTO(False, error=failure)
        path = self.ASSESSMENT_JOB_SUBMIT_FILTERED_PLAN.format(job_id)
        api_result = self._send_request(
            lambda: self.post(path, data.to_dict()), api_key, 'submit failure')
        return self._parse_api_result(api_result)

    def list_rule_results(self,
                          api_key: str,
                          assessment_id: Optional[str] = None,
                          result_status: Optional[str] = None,
                          enforcement_mode: Optional[RuleEnforcementModeDTO] = None,
                          policy_id: Optional[str] = None,
                          severity: Optional[RuleSeverityDTO] = None,
                          rule_type: Optional[RuleTypeDTO] = None,
                          security_layer: Optional[SecurityLayerDTO] = None,
                          resource_type: Optional[ResourceTypeDTO] = None,
                          start_date: Optional[int] = None,
                          end_date: Optional[int] = None,
                          query: Optional[str] = None):
        path = self.RULE_RESULTS_PATH.format(assessment_id or '',
                                             result_status or '',
                                             enforcement_mode.value if enforcement_mode else '',
                                             policy_id or '',
                                             severity.value if severity else '',
                                             rule_type.value if rule_type else '',
                                             security_layer.value if security_layer else '',
                                             resource_type.value if resource_type else '',
                                             query or '',
                                             start_date or '',
                                             end_date or '')
        api_result = self._send_request(lambda: self.get(path), api_key, 'list rule result')
        return self._parse_api_result(api_result, lambda x: [RuleResultDTO.from_dict(rl) for rl in x])

    def list_assessments_results(self,
                                 api_key: str,
                                 query: Optional[str] = None,
                                 origin: Optional[RunOriginDTO] = None,
                                 no_cloud_account: Optional[bool] = None,
                                 cloud_provider: Optional[CloudProviderDTO] = None,
                                 result_status: Optional[AssessmentResultTypeDTO] = None,
                                 cloud_account_id: str = None,
                                 sort_direction: Optional[str] = None,
                                 sort_by: Optional[str] = None,
                                 start_date: Optional[int] = None,
                                 end_date: Optional[int] = None,
                                 page: Optional[int] = None,
                                 items_per_page: Optional[int] = None
                                 ):
        no_cloud_account = '' if no_cloud_account is None else no_cloud_account.__str__().lower()
        path = self.ASSESSMENTS_RESULTS_PATH.format(query or '',
                                                    origin.value if origin else '',
                                                    no_cloud_account,
                                                    cloud_provider.value if cloud_provider else '',
                                                    result_status.value if result_status else '',
                                                    cloud_account_id or '',
                                                    start_date or '',
                                                    end_date or '',
                                                    page or '',
                                                    items_per_page or '',
                                                    sort_direction or '',
                                                    sort_by or '')

        def create_results(result):
            assessments = PaginationResultDTO.from_dict(result)
            assessments.page_results = [AssessmentResultDTO.from_dict(rl) for rl in assessments.page_results]
            return assessments

        api_result = self._send_request(lambda: self.get(path), api_key, 'list assessments results')
        return self._parse_api_result(api_result, create_results)

    def get_assessment_results(self, api_key: str, assessment_id: str):
        path = self.ASSESSMENTS_RESULTS_ID_PATH.format(assessment_id)
        api_result = self._send_request(lambda: self.get(path), api_key, 'get assessment results')
        return self._parse_api_result(api_result, AssessmentResultDTO.from_dict)

    def list_rules_tasks(self, api_key: str, query: Optional[str] = None):
        path = self.RULES_TASKS_PATH.format(query or '')
        api_result = self._send_request(lambda: self.get(path), api_key, 'list rule tasks')
        return self._parse_api_result(api_result, lambda x: [RuleTaskDTO.from_dict(rule_task) for rule_task in x])

    def get_rules_task_results(self, api_key: str, rule_id: str):
        path = self.RULES_TASK_RESULTS_PATH.format(rule_id)
        api_result = self._send_request(lambda: self.get(path), api_key, 'get rule task results')
        return self._parse_api_result(api_result, lambda x: [RuleResultDTO.from_dict(rule_result) for rule_result in x])

    def get_assessment_job(self, api_key: str, job_id: str) -> BaseCloudrailResponse:
        path = self.ASSESSMENT_JOB.format(job_id)
        api_result = self._send_request(lambda: self.get(path), api_key, 'get run status')
        return self._parse_api_result(api_result, AssessmentJobDTO.from_dict)

    def get_customer(self, customer_id, access_token=None, api_key=None):
        api_result = self._send_request(lambda: self.get(self.CUSTOMERS_PATH.format(customer_id)),
                                        custom_log_message='get customer',
                                        access_token=access_token,
                                        api_key=api_key)
        return self._parse_api_result(api_result, CustomerDTO.from_dict)

    def get_my_customer_data(self, access_token=None, api_key=None):
        api_result = self._send_request(lambda: self.get(self.CUSTOMERS_ME_PATH),
                                        custom_log_message='get my customer',
                                        access_token=access_token,
                                        api_key=api_key)
        return self._parse_api_result(api_result, CustomerDTO.from_dict)

    def generate_api_key_customer(self, access_token=None, api_key=None):
        api_result = self._send_request(lambda: self.post(self.CUSTOMERS_API_KEY_PATH),
                                        custom_log_message='generate api key customer',
                                        access_token=access_token,
                                        api_key=api_key)
        return self._parse_api_result(api_result, ApiKeyDTO.from_dict)

    def get_api_key_customer(self, access_token: str = None, api_key=None) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.CUSTOMERS_API_KEY_PATH),
                                        custom_log_message='get api key customer',
                                        access_token=access_token,
                                        api_key=api_key)

        def create_api_key_result(result):
            if result:
                return ApiKeyDTO.from_dict(result)
            return None

        return self._parse_api_result(api_result, create_api_key_result)

    def get_terraform_template(self, customer_id, access_token=None, api_key=None):
        api_result = self._send_request(lambda: self.get(self.CUSTOMERS_TERRAFORM_TEMPLATE_PATH.format(customer_id)),
                                        custom_log_message='get customer terraform template',
                                        access_token=access_token,
                                        api_key=api_key)
        if not api_result.success:
            return CloudrailErrorResponse(message=api_result.response)
        return CloudrailSuccessDataResponse(data=api_result.response)

    def list_rules(self,
                   api_key: str,
                   query: str = None,
                   policy_id: str = None,
                   has_policy_association: str = None,
                   severity: RuleSeverityDTO = None,
                   cloud_provider: CloudProviderDTO = None,
                   active: bool = None,
                   rule_type: RuleTypeDTO = None,
                   security_layer: SecurityLayerDTO = None,
                   resource_type: ResourceTypeDTO = None
                   ) -> BaseCloudrailResponse:
        policy_id = policy_id or ''
        query = query or ''
        has_policy_association = has_policy_association or ''
        active = active.__str__().lower() if active is not None else ''
        severity = severity.value if severity else ''
        cloud_provider = cloud_provider.value if cloud_provider else ''
        security_layer = security_layer.value if security_layer else ''
        rule_type = rule_type.value if rule_type else ''
        resource_type = resource_type.value if resource_type else ''
        api_result = self._send_request(lambda: self.get(self.LIST_RULES_PATH.format(query,
                                                                                     policy_id,
                                                                                     has_policy_association,
                                                                                     severity,
                                                                                     cloud_provider,
                                                                                     rule_type,
                                                                                     security_layer,
                                                                                     resource_type,
                                                                                     active)),
                                        api_key,
                                        'list rules')
        return self._parse_api_result(api_result, lambda x: [RuleInfoDTO.from_dict(rule) for rule in x])

    def get_rule(self, api_key: str, rule_id: str) -> BaseCloudrailResponse:
        api_result = self._send_request(lambda: self.get(self.RULE_ID_PATH.format(rule_id)),
                                        api_key,
                                        'get rule')
        return self._parse_api_result(api_result, RuleInfoDTO.from_dict)

    def update_rule(self, api_key: str, rule_id: str, rule_update_params: RuleUpdateDTO):
        api_result = self._send_request(lambda: self.patch(self.RULE_ID_PATH.format(rule_id), rule_update_params.to_dict()),
                                        api_key, 'update rule')
        return self._parse_api_result(api_result, RuleInfoDTO.from_dict)

    def update_rules(self, api_key: str, rule_updates_params: List[RuleBulkUpdateDTO]):
        rule_updates = RuleBulkUpdateDTO.schema().dumps(rule_updates_params, many=True)
        api_result = self._send_request(lambda: self.patch(self.UPDATE_RULES_PATH, data=rule_updates),
                                        api_key, 'update rules')
        return self._parse_api_result(api_result, lambda x: [RuleInfoDTO.from_dict(rule) for rule in x])

    def get_version(self):
        api_result = self._send_request(lambda: self.get(self.VERSION_PATH),
                                        custom_log_message='get version')
        return self._parse_api_result(api_result, lambda x: x['version'])

    def list_aws_supported_services(self):
        api_result = self._send_request(lambda: self.get(self.AWS_SUPPORTED_SERVICES),
                                        custom_log_message='list aws supported services')
        return self._parse_api_result(api_result, SupportedProviderServicesResponseDTO.from_dict)

    def list_azure_supported_services(self):
        api_result = self._send_request(lambda: self.get(self.AZURE_SUPPORTED_SERVICES),
                                        custom_log_message='list azure supported services')
        return self._parse_api_result(api_result, SupportedProviderServicesResponseDTO.from_dict)

    def list_checkov_supported_services(self, cloud_provider: CloudProviderDTO):
        api_result = self._send_request(lambda: self.get(self.CHECKOV_SUPPORTED_SERVICES.format(cloud_provider.value)),
                                        custom_log_message='list cechkov supported services')
        return self._parse_api_result(api_result, SupportedCheckovServicesResponseDTO.from_dict)

    def get_feature_flags(self, api_key: str, feature_flag_keys: List[str]):
        param = self._get_multiple_param_query('name', feature_flag_keys)
        api_result = self._send_request(lambda: self.get(self.FEATURE_FLAGS_PATH.format(param)), api_key, 'get feature flags')
        return self._parse_api_result(api_result, lambda x: x)

    def upload_log(self, log: str, job_id: str, command: str, api_key: str = None):
        api_result = self._send_request(
            lambda: self.post(self.UPLOAD_LOG.format(job_id, command), data=log), api_key, 'upload log')
        return self._parse_api_result(api_result)

    def list_rule_filters(self, api_key: str):
        api_result = self._send_request(lambda: self.get(self.RULE_FILTERS_PATH), api_key, 'get rule filters')
        return self._parse_api_result(api_result, lambda x: [FilterBlockDTO.from_dict(block) for block in x])

    def list_assessment_results_filters(self, api_key: str):
        api_result = self._send_request(lambda: self.get(self.ASSESSMENT_FILTERS_PATH), api_key, 'get assessment filters')
        return self._parse_api_result(api_result, lambda x: [FilterBlockDTO.from_dict(block) for block in x])

    def list_rule_results_filters(self, api_key: str):
        api_result = self._send_request(lambda: self.get(self.RULE_RESULT_FILTERS_PATH), api_key, 'get rule results filters')
        return self._parse_api_result(api_result, lambda x: [FilterBlockDTO.from_dict(block) for block in x])

    def account_connectivity_test(self, api_key: str, connectivity_test_request: ConnectivityTestRequestDTO):
        api_result = self._send_request(lambda: self.post(self.ACCOUNT_CONNECTIVITY_TEST, connectivity_test_request.to_dict()),
                                        api_key, 'account connectivity test')
        return self._parse_api_result(api_result, ConnectionTestDTO.from_dict)

    def list_latest_drift_detection_jobs(self, api_key):
        api_result = self._send_request(lambda: self.get(self.DRIFT_DETECTION_JOBS_LATEST_LIST),
                                        api_key, 'drift detection jobs latest list')
        return self._parse_api_result(api_result, lambda x: [DriftDetectionJobDTO.from_dict(j) for j in x])

    def get_drift_detection_results(self, job_id: str, api_key: str):
        api_result = self._send_request(lambda: self.get(self.DRIFT_DETECTION_RESULTS_GET.format(job_id)),
                                        api_key, 'drift detection results get')
        return self._parse_api_result(api_result, lambda x: x)

    def add_integration(self, data: AddUpdateExternalIntegrationDTO, api_key: str):
        api_result = self._send_request(lambda: self.post(self.INTEGRATIONS_PATH, data.to_dict()),
                                        api_key, 'integration add')
        return self._parse_api_result(api_result, ExternalIntegrationDTO.from_dict)

    def get_integration(self, integration_id: str, api_key: str):
        api_result = self._send_request(lambda: self.get(self.INTEGRATION_PATH.format(integration_id)),
                                        api_key, 'integration get')
        return self._parse_api_result(api_result, ExternalIntegrationDTO.from_dict)

    def update_integration(self, integration_id: str, data: AddUpdateExternalIntegrationDTO, api_key: str):
        api_result = self._send_request(lambda: self.patch(self.INTEGRATION_PATH.format(integration_id), data.to_dict()),
                                        api_key, 'integration update')
        return self._parse_api_result(api_result, ExternalIntegrationDTO.from_dict)

    def delete_integration(self, integration_id: str, api_key: str):
        api_result = self._send_request(lambda: self.delete(self.INTEGRATION_PATH.format(integration_id)),
                                        api_key, 'integration delete')
        return self._parse_api_result(api_result)

    def list_integrations(self, api_key: str):
        api_result = self._send_request(lambda: self.get(self.INTEGRATIONS_PATH),
                                        api_key, 'integration list')
        return self._parse_api_result(api_result, lambda x: [ExternalIntegrationDTO.from_dict(integ) for integ in x])

    @staticmethod
    def _get_multiple_param_query(key: str, values: List[str]):
        return '&'.join([f'{key}={value}' for value in values or []]) or ''

    @staticmethod
    def _parse_api_result(api_result: APIResult, success_response_function=None):
        if not api_result.success:
            if api_result.status == ApiStatus.UNAUTHORIZED:
                return CloudrailUnauthorizedResponse(message=api_result.response)
            return CloudrailErrorResponse(message=api_result.response)
        if not success_response_function:
            return CloudrailSuccessJsonResponse()
        return CloudrailSuccessJsonResponse(data=success_response_function(api_result.response))

    def _send_request(self, action, api_key: str = None, custom_log_message: str = '', access_token: str = None) -> APIResult:
        logging.debug(custom_log_message)
        if api_key:
            self.set_api_key(api_key)
        if access_token:
            self.set_access_token(access_token)
        try:
            response = action()
            self.unset_access_token()
            self.unset_api_key()

        except Exception:
            logging.exception(f'Failed to connect to the Cloudrail Service {self.api_base_url}')
            return APIResult(ApiStatus.FAILURE, f'Failed to connect to the Cloudrail Service {self.api_base_url}')
        if response.status_code == HTTPStatus.NO_CONTENT or not response.text:
            return APIResult(ApiStatus.SUCCESS, '')

        response_data = None
        if 'application/json' in response.headers['content-type']:
            response_data = json.loads(response.text)
        elif response.headers['content-type'] == 'application/octet-stream':
            response_data = response.text
        else:
            return APIResult(ApiStatus.FAILURE, 'Received unsupported content-type. Content-type can be application/json or text/plain')
        logging.debug('received data: {}'.format(response_data))

        if response.status_code != HTTPStatus.OK:
            if response.status_code == HTTPStatus.UNAUTHORIZED or response.status_code == HTTPStatus.FORBIDDEN:
                logging.error('Unauthorized request: {0}'.format(custom_log_message))
                return APIResult(ApiStatus.UNAUTHORIZED, 'Unauthorized. Please try to login again\n' + response_data['message'])

            message = 'Failed to {0}: {1}'.format(custom_log_message, response_data['message'])
            logging.error(message)
            return APIResult(ApiStatus.FAILURE, message)

        return APIResult(ApiStatus.SUCCESS, response_data)
