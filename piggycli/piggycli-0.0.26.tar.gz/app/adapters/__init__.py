import app.adapters.blockcypher_adapters as blockcypher

import datetime


class Explorer:
    def __init__(self, address):
        self.address = address
        address_data = _get_address_data(address=address)
        self.confirmed_balance = address_data['confirmed_balance']
        self.spent = address_data['spent']
        self.txrefs = _seralize_datetime(txrefs=address_data['txrefs'])


def _get_address_data(address):
    resp = blockcypher.address_data(address=address)

    return {
        'address': resp['address'],
        'confirmed_balance': resp['confirmed_balance'],
        'spent': resp['spent'],
        'txrefs': resp['txrefs']
    }


def _seralize_datetime(txrefs):
    for txref in txrefs:
        for k, v in txref.items():
            if isinstance(v, datetime.datetime):
                txref[k] = v.__str__()

    return txrefs


# def blockcypher_address_tx_inputs(txrefs):
#     tx_inputs = []
#     if bool(txrefs):
#         for txref in txrefs:
#             tx = {}
#             tx['output_no'] = txref['tx_output_n']
#             if tx['output_no'] < 0:
#                 tx['outpoint_index'] = ''
#                 tx['outpoint_hash'] = ''
#             else:
#                 tx['outpoint_index'] = (txref['tx_output_n']).to_bytes(
#                     4, byteorder='little', signed=False)
#                 hash = bytearray.fromhex(txref['tx_hash'])
#                 hash.reverse()
#                 tx['outpoint_hash'] = hash
#             tx_inputs.append(tx)
#     return tx_inputs
