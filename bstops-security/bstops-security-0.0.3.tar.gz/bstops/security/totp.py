#!/usr/bin/env python
# auth: walker

"""
Google Authenticator
"""

import pyotp
import base64
from io import BytesIO
from qrcode import QRCode, constants


class TOTP:

    def get_code(self, issuer, username):
        """
        Get QRCode token and image
        :param issuer:
        :param username:
        :return:
        """
        token = self.gen_token()
        url = self.bind(issuer, username, token)
        image = self.gen_qr_image(url)
        return token, image

    def to_base64(self, image, format='PNG'):
        """
        image to base64
        """
        buf = BytesIO()
        image.save(buf, format=format)
        image64 = base64.b64encode(buf.getvalue())
        return image64

    def gen_qr_image(self, url, size=6):
        qr = QRCode(
            version=1,
            error_correction=constants.ERROR_CORRECT_L,
            box_size=size,
            border=4)
        qr.add_data(url)
        qr.make(fit=True)
        image = qr.make_image()
        return image

    def gen_token(self):
        token = pyotp.random_base32(64)
        return token

    def bind(self, issuer, username, token):
        """
        绑定用户名
        :param issuer: 發行商
        :param username: 用戶名
        :return: URL(str)
        """
        otp = pyotp.totp.TOTP(token)
        url = otp.provisioning_uri(issuer_name=issuer, name=username)
        return url

    def verify(self, token, code):
        """
        驗證 Code
        :param token:
        :param code:
        :return:
        """
        otp = pyotp.TOTP(token)
        return otp.verify(code)
