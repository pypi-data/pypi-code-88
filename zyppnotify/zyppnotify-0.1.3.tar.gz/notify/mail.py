import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from pathlib import Path
from typing import Union
import logging
import pandas as pd

from notify.utils import check_environment_variables, dataframe_to_html


class NotifyMail:
    def __init__(
        self,
        to: str,
        subject: str,
        message: str,
        cc: str = None,
        files: Union[str, list] = None,
        df: pd.DataFrame = pd.DataFrame(),
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
        df: pd.DataFrame
            dataframe that needs to be added to the HTML message.
        """

        self.to = to
        self.cc = cc
        self.subject = subject
        self.message = message
        self.files = [files] if isinstance(files, str) else files

        check_environment_variables(["EMAIL_USER", "EMAIL_PW"])
        self.username = os.environ.get("EMAIL_USER")
        self.pw = os.environ.get("EMAIL_PW")
        self.df = df

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

        if self.df.shape[0] in range(1, 30):
            html_table = dataframe_to_html(df=self.df)
        elif self.df.shape[0] > 30:
            logging.warning(
                f"only first 30 records will be added.({self.df.shape[0]}> the limit of 30)."
            )
            html_table = dataframe_to_html(df=self.df.head(n=30))
        else:
            html_table = ""  # no data in dataframe (0 records)

        self.message += html_table
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
