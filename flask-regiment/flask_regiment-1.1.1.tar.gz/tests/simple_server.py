import os
from flask import Flask
from flask_regiment import BulletLog
from dotenv import load_dotenv
load_dotenv()
from simple_blueprint import bp

bulletlog = BulletLog()
print("bulletlog: loaded")

def create_app(test_config=None):
    print("create_app called")
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        BULLETLOG_API_KEY=os.getenv('API_KEY'),
        BULLETLOG_API_SECRET_KEY=os.getenv('API_SECRET_KEY'),
        BULLETLOG_META_DATA={
            "environment": "staging",
            "service_name": "test_app",
            "namespace": "zeroone"
        },
        BULLETLOG_LOG_TYPE='string'
    )
    print("bulletlog: initialized")

    bulletlog.init_app(app)
    print("bulletlog: registered")

    app.bulletlog.log_info("custom log from flask")
    print("bulletlog: custom log sent")

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
