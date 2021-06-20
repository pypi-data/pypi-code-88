import os
from flask import Flask
from flask_regiment import InstaLog
from dotenv import load_dotenv
load_dotenv()
from simple_blueprint import bp

instalog = InstaLog()
print("instalog: loaded")

def create_app(test_config=None):
    print("create_app called")
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        INSTALOG_API_KEY=os.getenv('API_KEY'),
        INSTALOG_API_SECRET_KEY=os.getenv('API_SECRET_KEY'),
        INSTALOG_META_DATA={
            "environment": "staging",
            "service_name": "test_app",
            "namespace": "zeroone"
        },
        INSTALOG_LOG_TYPE='string'
    )
    print("instalog: initialized")

    instalog.init_app(app)
    print("instalog: registered")

    app.instalog.log_info("custom log from flask")
    print("instalog: custom log sent")

    app.register_blueprint(bp, url_prefix='/bp')

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    @app.route('/e')
    def error():
        1/0
        return '', 200

    print("create_app done")

    return app
