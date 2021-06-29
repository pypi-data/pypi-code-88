settings = {
    'name': 'Mensajes de Texto',
    'icon_class': 'glyphicon glyphicon-envelope',
    'url': r'/sms/',
    'url_main_path': r'sms/',
    'users': [],
}

configuration_registers = (
    'SIC_SMS_NombreEmpresa',
    'SIC_SMS_TelDefault',
    'SIC_SMS_ApiKey',
    'SIC_SMS_MontoMinimo',
    'SIC_SMS_EnviarRemisionesPendientes',
    'SIC_SMS_ResumirMensajes',
    'SIC_SMS_InformacionExtra',
    'SIC_SMS_DiasPorVencer',
    'SIC_SMS_Saldo',
    'SIC_SMS_Ip_publica',
    'SIC_SMS_ModoPruebas'
    )

extrafields = (
    ('CLIENTES', 'SIC_SMS_NOENVIAR'),
)
