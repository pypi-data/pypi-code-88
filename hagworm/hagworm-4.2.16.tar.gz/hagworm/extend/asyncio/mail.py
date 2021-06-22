# -*- coding: utf-8 -*-

import aiosmtplib

from email.message import EmailMessage

from hagworm.extend.asyncio.base import Utils, AsyncCirculatorForSecond


class SMTPClient:

    def __init__(self, username, password, hostname, port, retry_count=5):

        self._username = username
        self._password = password

        self._hostname = hostname
        self._port = port

        self._retry_count = retry_count

    def create_message(self, sender, recipients, subject, content, _type=r'text/html'):

        message = EmailMessage()

        if sender is not None:
            message[r'From'] = sender

        if recipients is not None:
            message[r'To'] = recipients

        message[r'Subject'] = subject
        message.set_content(content)
        message.set_type(_type)

        return message

    def format_address(self, nickname, mailbox):

        return f'{nickname}<{mailbox}>'

    def format_addresses(self, items):

        return r';'.join(self.format_address(*item) for item in items)

    async def send_message(self, sender, recipients, message):

        resp = None

        async for times in AsyncCirculatorForSecond(max_times=self._retry_count):

            try:

                async with aiosmtplib.SMTP(hostname=self._hostname, port=self._port) as client:
                    await client.login(self._username, self._password)
                    resp = await client.send_message(message, sender, recipients)

            except aiosmtplib.SMTPException as err:

                if times >= self._retry_count:
                    raise err
                else:
                    Utils.log.warning(err)
                    continue

            except Exception as err:

                raise err

            else:

                break

        return resp

    async def send(self, sender, recipients, subject, content):

        return await self.send_message(
            sender, recipients,
            self.create_message(sender, recipients, subject, content)
        )
