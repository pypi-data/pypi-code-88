import re
from text2digits import text2digits
t2d = text2digits.Text2Digits()
def redact_msg(message):
        def normalize_redaction(word):
            if '{REDACTED}' in word:
                return '****'
            else:
                return word
        if message:
            text_numeric = t2d.convert(message)
            phrase_arr = re.sub('\d', '*', text_numeric)
            return  phrase_arr
        else:
            return message
def convert_pci_message(message):
    pci_msg = redact_msg(message)
    if re.search(r"(?<!\d)(\d{13}|\d{15}|\d{16}|\d{19})(?!\d)", pci_msg):
        pci_msg = re.sub(r"(?<!\d)(\d{13}|\d{15}|\d{16}|\d{19})(?!\d)", '****************', pci_msg)
    return pci_msg


x = convert_pci_message('make a 1 time payment')
print(x)