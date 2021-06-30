import requests #type: ignore

class WittyFlowSms:

    def __init__(self, app_id, app_secret):
        self.app_id     = app_id
        self.app_secret = app_secret

    def app_id(self):
        return self.app_id

    def app_secret(self):
        return self.app_secret

    def send_sms(self, phone, to, message, is_flash=False):

        body_to_send = {
            "from": f"{to}",
            "to":  f"233{phone[1:]}",
            "type": 1,
            "message": f"{message}",
            "app_id": f"{self.app_id}",
            "app_secret" : f"{self.app_secret}",
        }

        if is_flash:
            body_to_send["type"] = 0
        
        response = requests.post('https://api.wittyflow.com/v1/messages/send', data=body_to_send)
        return response.json()

    def get_account_balance(self):
        response = requests.get(f'https://api.wittyflow.com/v1/account/balance?app_id={self.app_id}&app_secret={self.app_secret}')
        return response.json()

    def check_sms_status(self, sms_id):
        response = requests.get(f'https://api.wittyflow.com/v1/messages/{sms_id}/retrieve?app_id={self.app_id}&app_secret={self.app_secret}')
        return response.json()