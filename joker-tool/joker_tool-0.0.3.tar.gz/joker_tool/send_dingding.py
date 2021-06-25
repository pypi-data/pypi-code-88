import requests
import json


class SendMessage(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_message(self, hook_url, message, at_mobiles=None):
        """
        :param hook_url: 钉钉机器人的url
        :param message: 需要发送的消息
        :param at_mobiles: 需要@的人,默认不@任何人,需要@多个人是用电话号码用逗号分开
        :return:
        """
        headers = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        string_text_msg = {
            "msgtype": "text",
            "text": {"content": message},
            "at": {}
        }
        if at_mobiles:
            if "," in at_mobiles:
                number = at_mobiles.split(",")
                string_text_msg["at"]['atMobiles'] = number
                string_text_msg['at']['isAtAll'] = False
            else:
                string_text_msg["at"]['atMobiles'] = [f"{at_mobiles}"]
                string_text_msg['at']['isAtAll'] = False
        else:
            string_text_msg["at"] = {
                "isAtAll": False
            }
        data = json.dumps(string_text_msg)
        print(data)
        res = requests.post(hook_url, data=data, headers=headers).status_code
        if res == "200":
            return "Message sent successfully"
        else:
            return "Message sending failed"


if __name__ == "__main__":
    s = SendMessage()
    s.send_message(
        "https://oapi.dingtalk.com/robot/send?access_token=45d9d79de773d0f9ba9ef2727b91ba0124a6c834001b835b2f5ee8f8ed4b7576",
        "监控测试")
