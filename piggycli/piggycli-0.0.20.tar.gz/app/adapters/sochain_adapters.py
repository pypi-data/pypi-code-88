import requests
import json


def get_confirmed_sat_balance(address):
    r = requests.get(
        f"https://sochain.com/api/v2/get_address_balance/BTC/{address}", timeout=5)
    assert r.status_code == 200, f'API returned a status_code of {r.status_code}, please try again later'
    resp = r.json()['data']
    btc_bal = resp['confirmed_balance']
    sat_bal = int(float(btc_bal) * 100000000)

    return sat_bal


def get_tx_inputs(address):
    resp = requests.get(
        f"https://sochain.com//api/v2/get_tx_unspent/BTC/{address}", timeout=5)
    assert resp.status_code == 200, f'block explorer return status code {resp.status_code}'
    resp_tx_inputs = resp.json()['data']['txs']
    assert not not resp_tx_inputs, f"Address: {address} has no unspent transactions"
    tx_inputs = []
    for resp_tx in resp_tx_inputs:
        tx = {}
        tx['output_no'] = resp_tx['output_no']
        tx['outpoint_index'] = (resp_tx['output_no']).to_bytes(
            4, byteorder='little', signed=False)
        hash = bytearray.fromhex(resp_tx['txid'])
        hash.reverse()
        tx['outpoint_hash'] = hash
        tx_inputs.append(tx)

    return tx_inputs
