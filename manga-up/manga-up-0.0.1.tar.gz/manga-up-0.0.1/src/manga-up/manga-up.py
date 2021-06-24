import requests

response = requests.get('https://httpbin.org/ip')
print('Code is {0}.'.format(response.status_code))