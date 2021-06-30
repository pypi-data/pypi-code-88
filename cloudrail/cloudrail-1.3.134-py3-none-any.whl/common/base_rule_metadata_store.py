import functools
from typing import List, Set, Optional, Dict

from cloudrail.knowledge.context.cloud_provider import CloudProvider
from cloudrail.knowledge.rules.rule_metadata import RuleMetadata, rule_matches_query, RuleSeverity, RuleType, SecurityLayer, ResourceType

from common.exceptions import NotFoundException

RULE_ID = 'rule_id'
NAME = 'name'
DESCRIPTION = 'description'
LOGIC = 'human_readable_logic'
CONSOLE_REMEDIATION_STEPS = 'console_remediation_steps'
IAC_REMEDIATION_STEPS = 'iac_remediation_steps'
SEVERITY = 'severity'
RULE_TYPE = 'rule_type'
SECURITY_LAYER = 'security_layer'
RESOURCE_TYPE = 'resource_type'
CLOUD_PROVIDER = 'cloud_provider'
RULE_METADATA_NOT_FOUND = 'Rule {} metadata not found'


class BaseRuleMetadataStore:
    def __init__(self, raw_metadata: dict):
        self.raw_metadata = raw_metadata
        if 'rules_metadata' not in self.raw_metadata:
            raise Exception('Rule metadata file must contain "rules_metadata" section.')

    def list_rules_metadata(self) -> List[RuleMetadata]:
        return list(self._get_rules_metadata().values())

    def list_rules_ids(self, provider: CloudProvider = None) -> Set[str]:
        if provider:
            return {metadata.rule_id for metadata in self._get_rules_metadata().values() if metadata.cloud_provider == provider}
        else:
            return set(self._get_rules_metadata().keys())

    def list_checkov_rule_ids(self, cloud_provider: Optional[CloudProvider] = None) -> List[str]:
        checkov_rules = [rule for rule in self._get_rules_metadata().values() if rule.rule_id.startswith('CKV_') and not rule.is_deleted]
        return [rule.rule_id for rule in checkov_rules if not cloud_provider or rule.cloud_provider == cloud_provider]

    def get_by_rule_id(self, rule_id: str) -> RuleMetadata:
        if rule_id not in self._get_rules_metadata():
            raise NotFoundException(RULE_METADATA_NOT_FOUND.format(rule_id))
        return self._get_rules_metadata()[rule_id]

    def query_rules_metadata(self, text: Optional[str]) -> List[RuleMetadata]:
        if not text:
            return self.list_rules_metadata()
        rules = []
        for rule in self.list_rules_metadata():
            if rule_matches_query(rule.rule_id, rule.name, text):
                rules.append(rule)
        return rules

    def merge(self, rule_metadata_store: 'BaseRuleMetadataStore'):
        self.raw_metadata = {'templates': self.raw_metadata.get('templates', []) + rule_metadata_store.raw_metadata.get('templates', []),
                             'rules_metadata': self.raw_metadata.get('rules_metadata', []) + rule_metadata_store.raw_metadata.get('rules_metadata',
                                                                                                                                  [])}
        self._get_rules_metadata.cache_clear()

    @staticmethod
    def _verify_all_fields_filled(rules):
        for rule in rules:
            if not rule.get(RULE_ID) \
                    or not rule.get(NAME) \
                    or not rule.get(DESCRIPTION) \
                    or not rule.get(LOGIC) \
                    or not rule.get(SEVERITY) \
                    or not rule.get(RULE_TYPE) \
                    or not rule.get(SECURITY_LAYER) \
                    or not rule.get(RESOURCE_TYPE):
                raise Exception(f'Invalid rule metadata {rule.get(RULE_ID) or rule}')

    @staticmethod
    def _verify_name_unique(rules):
        names = [rule[NAME] for rule in rules]
        if len(names) > len(set(names)):
            raise Exception('rule_id should be unique, duplicates: {}'.format({x for x in names if names.count(x) > 1}))

    @staticmethod
    def _verify_id_unique(rules):
        rule_ids = [rule[RULE_ID] for rule in rules]
        if len(rule_ids) > len(set(rule_ids)):
            raise Exception('rule_id should be unique, duplicates: {}'.format({x for x in rule_ids if rule_ids.count(x) > 1}))

    @staticmethod
    def _verify_rule_id_not_template(rules):
        if len(list(filter(lambda x: isinstance(x, dict), [rule[RULE_ID] for rule in rules]))) > 0:
            raise Exception('rule id can not be template based')

    @classmethod
    def _verify_rules(cls, rules):
        cls._verify_all_fields_filled(rules)
        cls._verify_name_unique(rules)
        cls._verify_id_unique(rules)
        cls._verify_rule_id_not_template(rules)

    @staticmethod
    def _fill_template(params_dict, templates):
        template_name = params_dict['template']
        if params_dict.get('params'):
            params = params_dict['params']
            for template in templates:
                for key, value in template.items():
                    if key == template_name:
                        return value.format(*tuple(params))
            return None
        else:
            for template in templates:
                for key, value in template.items():
                    if key == template_name:
                        return value
            return None

    @staticmethod
    def _is_template(value):
        if value is not None and isinstance(value, dict):
            return True
        return False

    @staticmethod
    def _fill_templates(rules, templates):
        for rule in rules:
            if BaseRuleMetadataStore._is_template(rule.get(NAME)):
                rule[NAME] = BaseRuleMetadataStore._fill_template(rule[NAME], templates)
            if BaseRuleMetadataStore._is_template(rule.get(DESCRIPTION)):
                rule[DESCRIPTION] = BaseRuleMetadataStore._fill_template(rule[DESCRIPTION], templates)
            if BaseRuleMetadataStore._is_template(rule.get(LOGIC)):
                rule[LOGIC] = BaseRuleMetadataStore._fill_template(rule[LOGIC], templates)
            if BaseRuleMetadataStore._is_template(rule.get(IAC_REMEDIATION_STEPS)):
                rule[IAC_REMEDIATION_STEPS] = BaseRuleMetadataStore._fill_template(rule[IAC_REMEDIATION_STEPS], templates)
            if BaseRuleMetadataStore._is_template(rule.get(CONSOLE_REMEDIATION_STEPS)):
                rule[CONSOLE_REMEDIATION_STEPS] = BaseRuleMetadataStore._fill_template(rule[CONSOLE_REMEDIATION_STEPS], templates)
        return rules

    @functools.lru_cache(maxsize=None)
    def _get_rules_metadata(self) -> Dict[str, RuleMetadata]:
        rules = self._fill_templates(self.raw_metadata['rules_metadata'], self.raw_metadata.get('templates', []))
        self._verify_rules(rules)
        return {rule[RULE_ID]: RuleMetadata(
            rule_id=rule[RULE_ID],
            name=rule[NAME],
            description=rule[DESCRIPTION],
            logic=rule[LOGIC],
            severity=RuleSeverity(rule[SEVERITY]),
            rule_type=RuleType(rule[RULE_TYPE]),
            security_layer=SecurityLayer(rule[SECURITY_LAYER]),
            resource_types={ResourceType(resource_type) for resource_type in rule[RESOURCE_TYPE]},
            iac_remediation_steps=rule.get(IAC_REMEDIATION_STEPS, ''),
            console_remediation_steps=rule.get(CONSOLE_REMEDIATION_STEPS, ''),
            cloud_provider=CloudProvider(rule[CLOUD_PROVIDER]),
            is_deleted=rule.get('is_deleted', False)) for rule in rules}
