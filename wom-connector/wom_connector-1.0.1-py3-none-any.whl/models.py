import json

class VoucherCreatePayloadEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, dict) \
                and 'Vouchers' in obj \
                and 'SourceId' in obj \
                and 'Nonce' in obj \
                and 'Password' in obj:
            obj

            return obj.to_JSON()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
