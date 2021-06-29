import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage


def send_tuner_message(send_to, message, subject):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('oraai.tuner@gmail.com', 'mtqcasvdyegrdcyy')
    msg = MIMEMultipart()
    msg['From'] = 'oraai.tuner@gmail.com'
    msg['To'] = send_to
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)


def send_complete_tuning_message(send_to, message, subject, reports=None):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login('oraai.tuner@gmail.com', 'mtqcasvdyegrdcyy')
    msg = EmailMessage()
    msg['From'] = 'oraai.tuner@gmail.com'
    msg['To'] = send_to
    msg['Subject'] = subject
    msg.set_content(message)
    if reports is not None:
        if isinstance(reports, list):
            for report in reports:
                with open(report, 'rb') as f:
                    file_data = f.read()
                msg.add_attachment(file_data, maintype="application", subtype="xls", filename=report.split("/")[-1])
        else:
            with open(reports, 'rb') as f:
                file_data = f.read()
            msg.add_attachment(file_data, maintype="application", subtype="xls", filename=reports.split("/")[-1])
    s.send_message(msg)


if __name__ == '__main__':
    send_complete_tuning_message(send_to="jedrzej@ora-ai.com", message="Tuning successfully finished",
                                 subject="Tuning successfully finished")
