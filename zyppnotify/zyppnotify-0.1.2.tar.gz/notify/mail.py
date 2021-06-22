import os
import smtplib
from typing import Union
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate

from notify.utils import check_environment_variables


class NotifyMail:
    def __init__(
        self, to: str, subject: str, message: str, cc: str = None, files: Union[str, list] = None
    ):
        """
        This function sends an e-mail from Microsoft Exchange server

        Parameters
        ----------
        to: str
            the e-mail adress to send email to
        subject: str
            subject of the message
        message:
            HTML or plain text content of the message
        cc: str
            e-mail adress to add as cc
        files: str, list
            Path(s) to file(s) to add as attachment
        """

        self.to = to
        self.cc = cc
        self.subject = subject
        self.message = message
        self.files = [files] if isinstance(files, str) else files

        check_environment_variables(["EMAIL_USER", "EMAIL_PW"])
        self.username = os.environ.get("EMAIL_USER")
        self.pw = os.environ.get("EMAIL_PW")

    def send_email(self) -> None:
        """
        This function sends an e-mail from Microsoft Exchange server

        Returns
        -------
        None
        """
        server = "smtp.office365.com"
        port = 587
        use_tls = True

        msg = MIMEMultipart()
        msg["From"] = self.username
        msg["To"] = self.to
        msg["Cc"] = self.cc
        msg["Date"] = formatdate(localtime=True)
        msg["Subject"] = self.subject

        msg.attach(MIMEText(self.message, "html"))

        # attach files if these are given else ignore
        if self.files:
            for path in self.files:
                part = MIMEBase("application", "octet-stream")
                with open(path, "rb") as file:
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                # Path(path).name grabs the filename from the path
                part.add_header("Content-Disposition", f"attachment; filename={Path(path).name}")
                msg.attach(part)

        smtp = smtplib.SMTP(server, port)
        if use_tls:
            smtp.starttls()

        smtp.login(self.username, self.pw)
        # smtp.sendmail(self.username, self.to, msg.as_string())
        smtp.send_message(msg=msg)
        smtp.quit()
