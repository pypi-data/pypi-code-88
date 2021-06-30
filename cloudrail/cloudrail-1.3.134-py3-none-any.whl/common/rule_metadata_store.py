from cloudrail.knowledge.context.cloud_provider import CloudProvider
from cloudrail.knowledge.rules.rule_metadata import get_rule_metadata_content

from common.base_rule_metadata_store import BaseRuleMetadataStore


def _get_internal_data():
    aws_data = get_rule_metadata_content(CloudProvider.AMAZON_WEB_SERVICES)
    azure_data = get_rule_metadata_content(CloudProvider.AZURE)

    all_data = {'templates': aws_data.get('templates', []) + azure_data.get('templates', []),
                'rules_metadata': aws_data.get('rules_metadata', []) + azure_data.get('rules_metadata', [])}
    return all_data


RuleMetadataStore = BaseRuleMetadataStore(_get_internal_data())
