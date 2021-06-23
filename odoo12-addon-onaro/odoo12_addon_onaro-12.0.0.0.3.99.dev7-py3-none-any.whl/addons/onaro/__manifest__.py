{
    'name': "Odoo customizations for Onaro",
    'version': '12.0.0.0.3',
    'author': "Coopdevs Treball SCCL",
    'depends': [
        'auth_api_key',
        'base',
        'base_rest',
        'crm_lead_product',
        'helpdesk_mgmt',
    ],
    'description': """
    Odoo Onaro customizations.
    """,
    'website': 'https://coopdevs.org',
    'category': "Cooperative management",
    'license': "AGPL-3",
    'data': [
        'views/crm_lead.xml',
        'security/res_users.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
