# Insert your code here. 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '724818342@qq.com'  # 发件人邮箱账号
my_pass = 'plxwxcsswjwfbccj'  # 发件人的邮箱授权码

def sendmail(receiver='724818342@qq.com', title='邮件测试', content='请在sendemail函数中定义title和content'):
    ret = True
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(["理山", my_sender])  # 括号里对应的分别是邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["强崽", receiver])  # 括号里的对应收件人邮箱昵称、收件人邮箱账
        msg['Subject'] = title  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SSL端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行成功，则会执行下面的 ret=False
        ret = False
    return ret

# ret = sendmail()
# if ret:
#     print("邮件发送成功！！！")
# else:
#     print("邮件发送失败！！！")
