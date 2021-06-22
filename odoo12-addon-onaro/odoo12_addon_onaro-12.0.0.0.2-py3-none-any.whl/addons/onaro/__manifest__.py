{
    'name': "Odoo customizations for Onaro",
    'version': '12.0.0.0.2',
    'author': "Coopdevs Treball SCCL",
    'depends': [
        'auth_api_key',
        'base',
        'base_rest',
        'crm_lead_product'
    ],
    'website': 'https://coopdevs.org',
    'category': "Cooperative management",
    'license': "AGPL-3",
    'data': [
        'views/crm_lead.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
