from sigur_interact.main import SigurSDK
from sigur_interact.tests import settings_test as s

sigur_sdk = SigurSDK(s.contr_ip, s.contr_port, 3, 1, 4, 2, test_mode=False)
print(sigur_sdk.get_auth_status())
print(sigur_sdk.get_elements_status())
sigur_sdk.subscribe_ce()
while True:
    response = sigur_sdk.sock.recv(1024)
    print(response)