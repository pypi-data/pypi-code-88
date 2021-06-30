from setuptools import setup

setup(
    name = 'AIRPrediction',
    version = '0.0.5',
    scripts = ['sampleapp.py', 'Time_Series_Models/prophet_model.py'],
    url = 'https://github.com/Data-for-Good-by-UF/AIRPrediction',
    license = 'MIT',
    install_requires = ['PySide2', 'pystan==2.19.1.1', 'prophet' 'aniso8601==9.0.1', 'click==8.0.1', 'colorama==0.4.4', 'Flask==2.0.1', 'Flask-RESTful==0.3.9', 'itsdangerous==2.0.1', 
    'Jinja2==3.0.1', 'MarkupSafe==2.0.1', 'numpy==1.21.0', 'pandas==1.2.5', 'patsy==0.5.1', 'pickleshare==0.7.5', 'python-dateutil==2.8.1', 
    'pytz==2021.1', 'scipy==1.7.0', 'six==1.16.0', 'statsmodels==0.12.2', 'Werkzeug==2.0.1'],
    data_files = ['pollution_us_2000_2016.csv']
)