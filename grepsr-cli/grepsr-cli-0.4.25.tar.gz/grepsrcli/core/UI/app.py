from threading import Condition
from grepsrcli.core.config import load_config
from webbrowser import open_new_tab
from flask import Flask, request, render_template


def load_ui(port):
    """this is main function for UI portion

     Args:
         port (int): the port in which the UI needs to be launched in the system
    """
    app = Flask(__name__)

    @app.route("/")
    def main():

        try:
            config = load_config('config.yml')
            platforms = {
                'PHP': config['php'],
                'Node': config['node'],
                'Python': config['python'],
                'PHP_Next': config['php_next']
            }

            return render_template('form2.html', config=config, platforms=platforms)
        except:
            return render_template('form.html')

    @app.route("/api")
    def api():
        return " Hello World API"

    @app.route('/config', methods=['POST'])
    def config():
        if request.method == 'POST':
            # process config and save it to configuration file

            f = request.environ.get("werkzeug.server.shutdown")
            f()
            return render_template('config.html')

    open_new_tab('0.0.0.0:' + str(port))
    app.run(debug=False, host="0.0.0.0", port=port)
