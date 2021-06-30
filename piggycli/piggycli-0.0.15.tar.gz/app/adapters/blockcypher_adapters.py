import blockcypher


def address_data(address):
    try:
        resp = blockcypher.get_address_details(address=address)

        return {
            'address': resp['address'],
            'confirmed_balance': resp['balance'],
            'txrefs': resp.get('txrefs'),
            'spent': is_spent(data=resp)
        }

    except AssertionError as e:
        raise AddressNotValid(e.args[0])

    except Exception as e:
        raise Exception(e.args[0])


def is_spent(data):
    if data['total_sent'] > 0:
        return True
    else:
        return False


class AddressNotValid(Exception):
    pass
