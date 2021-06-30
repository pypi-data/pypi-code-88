from app.utilities.bitcoin.tx_scripts import TxOutputScript, PubKeyScript
from app.utilities.bitcoin.addresses import P2PKH
from app.adapters import Explorer

import hashlib


class UnsignedTx:

    def __init__(self, address, recipient, fee, value, change_address):
        self.confirmed_balance = address.confirmed_balance
        self.tx_outs = TxOutputScript(
            address=address.address,
            confirmed_balance=address.confirmed_balance,
            recipient=recipient,
            fee=fee,
            value=value,
            change_address=change_address
        )
        self.pub_key_script = PubKeyScript(address=address.address)
        self.txrefs = address.txrefs

    @property
    def messages(self):
        messages = []
        for tx in self.tx_inputs:
            msg = bytearray()
            msg += self.version
            msg += self.tx_in_count
            for tx_in in self.tx_inputs:
                msg += self.previous_output(tx_in)
                if tx == tx_in:
                    msg += self.pub_key_script.bytes
                    msg += self.pub_key_script.script
                else:
                    msg += self.placeholder
                msg += self.sequence
            msg += self.tx_out_count
            for tx_output in self.tx_outs.outputs:
                msg += tx_output
            msg += self.lock_time
            msg += self.hash_code

            messages.append({'message': msg, 'tx_input': tx})

        return messages

    @property
    def to_sign(self):
        to_signs = []
        for msg in self.messages:
            to_signs.append(hashlib.sha256(msg['message']).digest())
        return to_signs

    @property
    def version(self):
        return (1).to_bytes(4, byteorder="little", signed=True)

    @property
    def tx_inputs(self):
        tx_inputs = []
        if bool(self.txrefs):
            for txref in self.txrefs:
                tx_input = {'output_no': txref['tx_output_n'],
                            'outpoint_index': None, 'outpoint_hash': None}
                if tx_input['output_no'] >= 0:
                    tx_input['outpoint_index'] = (txref['tx_output_n']).to_bytes(
                        4, byteorder='little', signed=False)
                    hash = bytearray.fromhex(txref['tx_hash'])
                    hash.reverse()
                    tx_input['outpoint_hash'] = hash
                tx_inputs.append(tx_input)
        return tx_inputs

    @property
    def tx_in_count(self):
        return (len(self.tx_inputs)).to_bytes(1, byteorder="little", signed=False)

    def previous_output(self, tx_in):
        output = bytearray()
        output += tx_in['outpoint_hash']
        output += tx_in['outpoint_index']
        return output

    @property
    def placeholder(self):
        return (0).to_bytes(1, byteorder='little', signed=False)

    @property
    def sequence(self):
        return bytes.fromhex("ffffffff")

    @property
    def tx_out_count(self):
        return (len(self.tx_outs.outputs)).to_bytes(1, byteorder="little", signed=False)

    @property
    def lock_time(self):
        return (0).to_bytes(4, byteorder="little", signed=False)

    @property
    def hash_code(self):
        return (1).to_bytes(4, byteorder='little', signed=False)
