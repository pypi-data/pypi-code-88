from feapder.utils import tools

EAMIL_SENDER = "feapder@163.com"  # 发件人
EAMIL_PASSWORD = "YPVZHXFVVDPCJGTH"  # 授权码
EMAIL_RECEIVER = "564773807@qq.com"  # 收件人 支持列表，可指定多个
# 时间间隔
WARNING_INTERVAL = 3600  # 相同报警的报警时间间隔，防止刷屏
WARNING_LEVEL = "DEBUG"  # 报警级别， DEBUG / ERROR
EMAIL_SMTPSERVER="smtp.163.com"


tools.email_warning(
    message="test3",
    title="test",
    message_prefix=None,
    eamil_sender=EAMIL_SENDER,
    eamil_password=EAMIL_PASSWORD,
    email_receiver=EMAIL_RECEIVER,
    rate_limit=WARNING_INTERVAL,
    email_smtpserver=EMAIL_SMTPSERVER
)
