from base58 import b58decode_check
import hashlib
from ecdsa import SECP256k1, VerifyingKey, util


class TxOutputScript():

    def __init__(self, address, confirmed_balance, recipient, fee, value, change_address):
        assert address != change_address, 'An address cannot send change to itself'
        self.confirmed_balance = confirmed_balance
        self.recipient = recipient
        self.fee = fee
        self.value = value
        self.change_address = change_address

    @property
    def outputs(self):
        assert self.fee > 0, 'fee must be greater than zero'
        assert self.verify_address(
            self.recipient), 'reipient address is not valid'
        if self.value is None:
            self.value = self.confirmed_balance - self.fee
        else:
            assert self.value > 0, 'quantity must be greater than zero'
            assert self.confirmed_balance >= self.value + \
                self.fee, 'quanity + fee cannot be greater than confirmed balance'

        outputs = []
        outputs.append(self.output(self.value, self.recipient))

        if self.value + self.fee < self.confirmed_balance:
            assert self.verify_address(
                self.change_address), 'change address is not valid'
            change_value = self.confirmed_balance - self.value - self.fee
            outputs.append(self.output(change_value, self.change_address))

        return outputs

    def verify_address(self, address):
        # TO DO
        return True

    def output(self, value, address):
        pub_key_script = PubKeyScript(address)
        output = bytearray()
        output += (value).to_bytes(8, byteorder="little", signed=False)
        output += pub_key_script.bytes
        output += pub_key_script.script

        return output


class PubKeyScript():

    def __init__(self, address):
        self.address = address
        pass

    @property
    def script(self):
        if self.address[0] == '1':
            return self.p2pkh_pk_script
        elif self.address[0] == '3':
            return self.p2sh_pk_script
        else:
            raise ('Only P2PKH and P2SH addresses are supported')

    @property
    def bytes(self):
        return len(self.script).to_bytes(
            1, byteorder='little', signed=False)

    @property
    def addressToPubKeyHash(self):
        return b58decode_check(self.address)[1:]

    @property
    def p2pkh_pk_script(self):
        script = bytearray()
        script += bytearray.fromhex('76')  # OP_DUP
        script += bytearray.fromhex('a9')  # OP_HASH
        script += bytearray.fromhex('14')  # Push 20 bytes as Data
        script += self.addressToPubKeyHash
        script += bytearray.fromhex('88')  # OP_EQUALVERIFY
        script += bytearray.fromhex('ac')  # OP_CHECKSIG
        return script

    @property
    def p2sh_pk_script(self):
        script = bytearray()
        script += bytearray.fromhex('a9')  # OP_HASH
        script += bytearray.fromhex('14')  # Push 20 bytes as Data
        script += self.addressToPubKeyHash
        script += bytearray.fromhex('87')  # OP_EQUAL
        return script


class SigScript():

    def __init__(self, signatures, unsigned_tx, tx_in, pem):
        self.signatures = signatures
        self.unsigned_tx = unsigned_tx
        self.tx_in = tx_in
        self.pem = pem

    @property
    def signature(self):
        for msg in self.unsigned_tx.messages:
            if msg['tx_input'] == self.tx_in:
                message = msg['message']

        for signature in self.signatures:

            if self.verify_der_signature(signature, message, self.pem):
                return self.der_canonize(signature)

        raise SingatureNotValid('Signatures are not valid')

    @property
    def signature_bytes(self):
        return (len(self.signature) + 1).to_bytes(1,
                                                  byteorder='little',
                                                  signed=False)

    @property
    def public_key(self):
        vk = VerifyingKey.from_pem(self.pem)
        return bytes.fromhex('04') + vk.to_string()

    @property
    def public_key_bytes(self):
        return (len(self.public_key)).to_bytes(1,
                                               byteorder="little",
                                               signed=False)

    @property
    def script(self):
        sig_script = bytearray()
        sig_script += self.signature_bytes
        sig_script += self.signature
        sig_script += bytes.fromhex('01')
        sig_script += self.public_key_bytes
        sig_script += self.public_key
        return sig_script

    @property
    def script_bytes(self):
        return (len(self.script)).to_bytes(1,
                                           byteorder='little',
                                           signed=False)

    def verify_der_signature(self, signature, message, pem):
        double_hashed_message = hashlib.sha256(
            hashlib.sha256(message).digest()).digest()

        try:
            vk = VerifyingKey.from_pem(pem)
            vk.verify_digest(signature, double_hashed_message,
                             sigdecode=util.sigdecode_der)
            return True
        except Exception:
            return False

    def der_canonize(self, signature):
        r, s = util.sigdecode_der(signature, SECP256k1.order)
        return util.sigencode_der_canonize(r, s, SECP256k1.order)


class SingatureNotValid(Exception):
    pass
