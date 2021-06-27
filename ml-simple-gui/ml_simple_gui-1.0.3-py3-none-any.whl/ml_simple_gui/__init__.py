from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from .utils import check_model, calculate_sensitivity, calculate_specificity, get_data_from_csv
import os
import json


class Application:
    model = None
    model_constructor = None
    upload_path = '/upload'
    server_port = 5000
    csv_delimiter = ','
    model_params = [
        {
            'code': 'testPercent',
            'name': 'Процент тестовой выборки',
            'defaultValue': 25,
        }
    ]

    def __init__(self, model, upload_path, csv_delimiter, model_params=None, server_port=5000):
        if model_params is None:
            model_params = []
        if callable(model):
            self.model_constructor = model
        else:
            self.model = model
        self.upload_path = upload_path
        self.csv_delimiter = csv_delimiter
        self.server_port = server_port
        self.model_params += model_params
        self.process_model_params()

    def set_model(self, model):
        self.model = model
        return self

    def set_upload_path(self, upload_path):
        self.upload_path = upload_path
        return self

    def set_server_port(self, port):
        self.server_port = port
        return self

    def set_csv_delimiter(self, csv_delimiter):
        self.csv_delimiter = csv_delimiter
        return self

    def run(self):
        flask_app = Flask(
            __name__,
            static_url_path='',
            static_folder='./frontend/dist',
            template_folder='./frontend/dist'
        )
        flask_app.debug = True
        flask_app.config['UPLOAD_FOLDER'] = self.upload_path
        CORS(flask_app)

        self.set_routes(flask_app)

        flask_app.run(port=self.server_port)

    def process_model_params(self):
        for k in range(len(self.model_params)):
            if 'value' not in self.model_params[k]:
                self.model_params[k]['value'] = self.model_params[k]['defaultValue']

    def set_routes(self, app):
        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/model_params')
        def model_params():
            return jsonify({
                'status': 'success',
                'result': {
                    'params': self.model_params
                }
            })

        @app.route('/upload_data/', methods=['POST'])
        def upload_data():
            file = request.files['file']
            if file:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)
                return jsonify({
                    'status': 'success',
                    'result': {
                        'file_path': file.filename
                    }
                })
            else:
                return jsonify({
                    'status': 'error',
                    'result': {
                        'message': 'Неподходящий тип файла'
                    }
                })

        @app.route('/fit_predict/', methods=['POST'])
        def fit_predict():
            # {'file': {'file_path': 'test.csv'}, 'modelParams': {}}
            req_params = json.loads(request.get_data())
            if len(req_params['file']['file_path']) == 0 or not os.path.isfile(
                    os.path.join(self.upload_path, req_params['file']['file_path'])):
                return jsonify({
                    'status': 'error',
                    'result': {
                        'message': 'Файл не существует'
                    }
                })
            if self.model_constructor:
                params = {}
                for paramCode in req_params['modelParams']:
                    if paramCode == 'testPercent':
                        continue
                    params[paramCode] = req_params['modelParams'][paramCode]['value']
                self.model = self.model_constructor(**params)
            if not check_model(self.model):
                return jsonify({
                    'status': 'error',
                    'result': {
                        'message': 'Ошибка при использовании модели. Проверьте наличие необходимых методов'
                    }
                })
            data_from_file = get_data_from_csv(
                os.path.join(self.upload_path, req_params['file']['file_path']), self.csv_delimiter)
            x = data_from_file.iloc[:, :-1]
            y = data_from_file.iloc[:, -1:]

            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=int(
                req_params['modelParams']['testPercent']['value']) / 100)

            self.model.fit(x_train, y_train)
            y_pred = self.model.predict(x_test)

            accuracy = accuracy_score(y_test, y_pred)
            sensitivity = calculate_sensitivity(y_test, y_pred) * 100
            specificity = calculate_specificity(y_test, y_pred) * 100

            return jsonify({
                'status': 'success',
                'result': {
                    'accuracy': accuracy,
                    'sensitivity': sensitivity,
                    'specificity': specificity,
                }
            })
