from sigur_interact.functions import send_sigur_command
from sigur_interact.tests.main_test import sigur_sdk


response = send_sigur_command(sigur_sdk.sock, "man")
print("response:", response)