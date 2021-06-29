from zalo_official.oa.OaInfo import OaInfo
from zalo_official.oa.OaClient import OaClient
from zalo_official.app.AppInfo import AppInfo
from zalo_official.app.AppClient import AppClient
import requests

app_id = '557135423935002466'
secret_key = 'vbRlENYRd8mWv4T7MjmZ'
callback_url = 'https://tiendq.requestcatcher.com/'
user_id = '7412339252416577980'
code = 'nta8CqI-0NZZFom7OBK12kDQBdaliIiGh5HQS3osUJ6DL5vz7zHq09uiIYGZ_sDNvX9ZCcB30KBU71ODPEi8S_Th8GXouoKg-0KsIWVMDIg794Pu1kHLEhK8Ia5Yd4OHdqiOLNZ1P3gnCcPBAgD5GlCZ4ri3YG4pw5De6pJBR2QX3JurVOWiLVuBNmeHqLHSqsCDU1I0TLVlKILLKeSDEuuH8byTvIjz-KP59rhe1GITV5yiJgyKAEKVR1fggp4bzZS2IMQAGLc4EW7n9huSlRP-EQ0vk22WpMKQqNcw22EU2mfJ7Sdfapa1zDw9kV6YGWZFfvg7sA9t0hoTxQMsf4Stpgooe9R5K3tcjbac8RW4EdESAaK'
token = 'rDkPRbednqJNs9bYNI34JTRPdsH1MfitclcVU7L3lW6xsQ8fRM6jVBBjzmjeP-zxk-Bx1KuTqqAWiTiPLmpnFeYuq1DQ4_HuZk_3FK4M-tUWZ_uUBn7NDUUem1Ci0CD8pABqOJS2wapfz-OAFGl-JzMKmWGb5CL8shJu9LS0zctMlleeDHQlGVZkZmqlLwrwmywZBnnbztQGdEek46B4U9t3_oyLIVz5s-NgR317jYlUoEbV35pK2iNUr24DHz1LnVd5UaaDoYR3Zf9151MMPsIvpMqVNZZ1H0'
access_token = '01q0VsLAb7a37W1pOasNS08V1dL-EFO972qqJ2CwvmOq6t9_3Hgn81LFKMOc4APcBYHU854He40x62eH1nFkRYynUHS5Efbg8nTc5Zr1W7GfT65t5a2C1nv5Q5LrLA0sJs1eObyhe3rgUqn_TIkU3NO9V51BNhbRJKyp8r16vIawPnfS77Nd6oj1D14I4T17DJrF8nG1cLGr7MuX7H25O7SkG3yG9QPu5tfr0Z4ikKKHAryF2W6H3MfASrqEJfa75qbvUYPsjpu6NMHRCtgGC0raMaSxQR53TKTNKcQdCs5Lada'
zalo_info = OaInfo(oa_id=None, secret_key=secret_key)
zalo_oa_client = OaClient(zalo_info)


profile = zalo_oa_client.get('getoa', {'access_token': access_token})
print(profile)

def send_request(endpoint, params):
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.get(url=endpoint, params=params, headers=headers)
    return response.json()


# tien_id = '2057041539176770285'
# zalo_info = ZaloAppInfo(app_id=app_id, secret_key=secret_key, callback_url=callback_url)
# zalo_3rd_app_client = Zalo3rdAppClient(zalo_info)
# login_url = zalo_3rd_app_client.get_login_url()
# print(login_url)
# token = zalo_3rd_app_client.get_access_token(code)['access_token']
# print(access_token)
# friends = zalo_3rd_app_client.get('/me/friends', token, {'offset': 10, 'limit': 50})
# print(friends)
# data = send_request(friends['paging']['previous'], {})
# print(data)
# invitable_friends = zalo_3rd_app_client.get('/me/invitable_friends', token, {
#     'offset': '0',
#     'limit': '10',
#     'fields': 'id, name, birthday, gender, picture'
# })
# print(invitable_friends)
# send_message = zalo_3rd_app_client.post('/me/message', token, {
#     'message': 'Noi dung test phat nua',
#     'to': tien_id,
#     'link': 'https://developers.zalo.me/'
# })
# print(send_message)
# oainfo = zalo_oa_client.get('getoa', {'access_token': access_token})
# print(oainfo['data']['oa_id'])
follows = zalo_oa_client.get('getfollowers', {'access_token': access_token, 'data': {'offset': 0, 'count': 50}})
print(follows)
# listchats = zalo_oa_client.get('listrecentchat', {'access_token': access_token, 'data': {'offset': 0, 'count': 10}})
# print(listchats)
# conversations = zalo_oa_client.get('conversation', {'access_token': access_token, 'data': {'user_id': 615280704370294525, 'offset': 0, 'count': 10}})
# print(conversations)
# msgs = zalo_oa_client.post('message', {
#     'access_token': access_token,
#     'data': {
#         'recipient': {'user_id': 2057041539176770285},
#         'message': {
#             'text': 'test thu phat nua'
#         }
#     }
# })
# print(msgs)
