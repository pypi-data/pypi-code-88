import json

from py_eureka_client import eureka_client

from ml_platform_client.config import client_config
from ml_platform_client.dispatcher import register
from ml_platform_client.server import app
from ml_platform_client.server import set_preload_models
from example.basic.algorithms import MyAlgorithm, FakeAlgorithm

minio_host = '172.16.99.29:9000'
minio_access_key = '24WTCKX23M0MRI6BA72Y'
minio_secret_key = '6mxoQMf1Lha2q1H3fp3fjNHEZRJJ7LvbC5k3+CQX'
minio_secure = False
mysql_host = '172.16.99.29'
mysql_port = 3306
mysql_user = 'root'
mysql_password = 'password'

if __name__ == '__main__':
    client_config.minio_host = minio_host
    client_config.minio_access_key = minio_access_key
    client_config.minio_secret_key = minio_secret_key
    client_config.minio_secure = minio_secure

    client_config.mysql_host = mysql_host
    client_config.mysql_port = mysql_port
    client_config.mysql_user = mysql_user
    client_config.mysql_password = mysql_password

    register('my_alg', MyAlgorithm)
    register('fake_alg', FakeAlgorithm)
    set_preload_models('my_alg', ['pretrain_model_id1', 'pretrain_model_id2'])

    my_alg_meta = {
        'identifier': 'my_alg',
        'type': 'text_classification',
        'trainable': True,
        'standalone_train': True,
        'name': '分类算法-myalg',
        'description': '测试测试'
    }

    metadata = {
        'algorithm.my_alg': json.dumps(my_alg_meta)
    }

    eureka_client.init(
        eureka_server='http://peer1:8849/mlp/eureka/,http://peer2:8850/mlp/eureka/,http://peer3:8851/mlp/eureka/',
        app_name='simple-alg',
        instance_port=6666,
        metadata=metadata,
        renewal_interval_in_secs=5,
        duration_in_secs=15
    )

    app.run(port=6666)
