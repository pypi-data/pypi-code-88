# -*- coding: utf-8 -*-
"""
@author: wuhaoyu

@description：邮件发送模块
"""
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def send_mail(host, port, user, password, receivers, subject, **kwargs):
    """
    host: 邮箱IP
    port: 邮箱服务端口
    user: 邮箱认证账号
    password: 认证账号密码
    receivers: 收件人列表
    subject: 邮件主题
    kwargs: from_mask\receivers_mask\carbon_copy\carbon_copy_mask\content\attaches
    """
    # 加载配置
    from_ = kwargs.get("from_mask", user)
    to = kwargs.get("receivers_mask", receivers)
    carbon_copy = kwargs.get("carbon_copy", [])
    carbon_copy_mask = kwargs.get("carbon_copy_mask", [])
    
    # 创建一个带邮件实例
    message = MIMEMultipart()
    message['From'] = Header(from_, 'utf-8')
    message['To'] = Header(",".join(to), 'utf-8')
    message['Cc'] = Header(",".join(carbon_copy_mask), 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    content = kwargs.get('content', '')
    message.attach(MIMEText(content, 'plain', 'utf-8'))
    
    # 附件子模块
    attaches = kwargs.get("attaches", None)
    if attaches:
        for attach in attaches:
            with open(attach, 'rb') as f:
                file = f.read()
            att = MIMEText(file, 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att.add_header("Content-Disposition", "attachment", filename=("gbk", "", os.path.split(attach)[-1]))
            message.attach(att)
    
    # 连接邮箱服务器
    smtp_obj = smtplib.SMTP_SSL(host, port)
    smtp_obj.login(user, password)
    try:
        smtp_obj.sendmail(user, list(set(receivers + carbon_copy)), message.as_string())
        print(f"邮件【{subject}】发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    finally:
        smtp_obj.close()
