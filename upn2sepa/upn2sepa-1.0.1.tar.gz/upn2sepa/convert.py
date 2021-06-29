from PIL import Image
from pyzbar.pyzbar import decode
from segno import helpers


def convert(path):
    data = decode(Image.open(path))
    raw_text = data[0][0]
    utf8_text = raw_text.decode("utf-8")

    # Decoding content of UPN QR
    # https://www.upn-qr.si/uploads/files/NavodilaZaProgramerjeUPNQR.pdf

    decoded = utf8_text.split("\n")
    print(decoded)
    type = decoded[0]
    # sender_name = decoded[5]
    # sender_address = decoded[6]
    # sender_city = decoded[7]
    amount = int(decoded[8])
    purpose_code = decoded[11]
    # purpose = decoded[12]
    # deadline = decoded[13]
    iban = decoded[14]
    reference = decoded[15]
    receiver_name = decoded[16]
    # receiver_address = decoded[17]
    # receiver_city = decoded[18]
    # control_sum = decoded[19]

    qr = helpers.make_epc_qr(name=receiver_name,
                             iban=iban,
                             amount=amount/100,
                             text=None,
                             reference=reference,
                             bic=None,
                             purpose=purpose_code,
                             encoding=None
                             )
    qr.show()
