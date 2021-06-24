from amazondax import SigV4Gen

import datetime

from collections import namedtuple

FakeCreds = namedtuple('FakeCreds', 'access_key secret_key token')

DAX_ADDR = 'https://dax.amazonaws.com'
REGION = 'us-east-1'
NOW = datetime.datetime(2017, 4, 21, 15, 54, 58)
ACCESS_KEY = ''
SECRET_KEY = '4UcEo9UVroGJBjyIocpXPCLVSYUM1SW2ESvixmtJ'


def test_generate_sig():
    creds = FakeCreds(ACCESS_KEY, SECRET_KEY, None)
    actual = SigV4Gen.generate_signature(creds, DAX_ADDR, REGION, b'', NOW)
    # Expected result taken from DAX JavaScript client
    expected = SigV4Gen.Signature(
        'e8efcbe71d76c6889b08e0e661a0cadbc0d81d484901d20538837d2c8aaa6bc5',
        'AWS4-HMAC-SHA256\n20170421T155458Z\n20170421/us-east-1/dax/aws4_request\n308f4b7cd2bcf9ba1b1cdcfd7457d50698754fea9ab590dbafc28eac9dcb4b79',
        None)

    assert actual == expected

def test_generate_sig_token():
    TOKEN = 'FQoDYXdzEEwaDLfCB2cj1bsNWfGv0SLSAWoXkChQ5fMA8mF5m+GNG7oB9YZKz53itsOVUTCJTkZFtt75UeEmDLiwvzoecAKvGvg0vOPYeXLFec9ZEGaTpNlL/+6L4eAw+ND9q+uLDR50vIJbxbG1GUKruijKEd9cqyZLwNDjn7RWEUn6qzZlGeGtJzZy0nAuaY7Nz6IrvUyUBOBIDgcsQn09wrRm//06/UX/QHp+mieBGygx/40ktJK/XkW/DguS1YKhAQMmUQmyayLoB4Vdn+amNZ2KANBbARNEgnEnVoAjUH+aFjKqGAC79SillbTLBQ=='

    creds = FakeCreds(ACCESS_KEY, SECRET_KEY, TOKEN)
    actual = SigV4Gen.generate_signature(creds, DAX_ADDR, REGION, b'', NOW)
    # Expected result taken from DAX JavaScript client
    expected = SigV4Gen.Signature(
        'e8efcbe71d76c6889b08e0e661a0cadbc0d81d484901d20538837d2c8aaa6bc5',
        'AWS4-HMAC-SHA256\n20170421T155458Z\n20170421/us-east-1/dax/aws4_request\n308f4b7cd2bcf9ba1b1cdcfd7457d50698754fea9ab590dbafc28eac9dcb4b79',
        TOKEN)

    assert actual == expected

