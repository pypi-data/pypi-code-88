from flask_scenario_testing.conduit.create_app import create_app
from flask_scenario_testing.conduit.settings import ProdConfig

app = create_app(ProdConfig())
