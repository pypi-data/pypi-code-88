import requests
from libra_core.log import log_info
from libra_core.utils import sleep, load_json, dump_json
from libra_core.wrapper import try_catch_exception
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os


@try_catch_exception
def send_sms(msg, phone):
    log_info("start send_sms for phone={} msg={}".format(phone, msg))
    message_api_url = "https://op-manage.apuscn.com/smshandle/smsapi/"
    data = {
        "stype": 'faf05cee-69b9-11ea-937d-fa163e911b2d',
        "msg": msg,
        "to_user": phone,
        "type": 'sms',
        "directly": True,
    }
    headers = {"Authorization": "application/json"}
    resp = requests.post(message_api_url, headers=headers, data=dump_json(data).encode())
    sleep(1)
    jsd = load_json(resp.text)
    log_info("done send_sms for phone={} msg={} result={}".format(phone, msg, resp.text))
    if not jsd or jsd.get('status') != 'ok':
        return False
    return True


__mail_host = "mail.apusapps.com"  # 设置服务器
__port = 465
__mail_user = "notify-ee"  # 用户名
__mail_pass = "go6+E=uqxOzS%6zC"  # 口令
__mail_postfix = "apusapps.com"  # 发件箱的后缀


@try_catch_exception
def send_mail(sub, content, emails, file_list=None):
    global __mail_host, __port, __mail_user, __mail_pass, __mail_postfix
    log_info("start send_mail sub={} for emails={}".format(sub, emails))
    me = __mail_user + "@" + __mail_postfix
    msg = MIMEMultipart()
    msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(emails)
    if file_list:
        for f in file_list:
            part = MIMEBase('application', 'octet-stream')  # 'octet-stream': binary data
            part.set_payload(open(f, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)
    server = smtplib.SMTP_SSL(host=__mail_host, timeout=20)
    server.connect(__mail_host, __port)
    server.login(__mail_user, __mail_pass)
    server.sendmail(me, emails, msg.as_string())
    server.close()
    log_info("done send_mail sub={} for emails={}".format(sub, emails))
    return True


def try_send_mail(sub, content, emails, file_list=None, retry_count=3):
    while retry_count > 0:
        if send_mail(sub, content, emails, file_list):
            return True
        sleep(2)
        retry_count -= 1
    return False
