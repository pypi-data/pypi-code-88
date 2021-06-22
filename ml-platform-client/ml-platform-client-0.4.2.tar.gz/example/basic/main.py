from example.basic.algorithms import MyAlgorithm, FakeAlgorithm
from ml_platform_client.config import client_config
from ml_platform_client.dispatcher import register
from ml_platform_client.server import app

minio_host = '172.16.99.29:9000'
minio_access_key = '24WTCKX23M0MRI6BA72Y'
minio_secret_key = '6mxoQMf1Lha2q1H3fp3fjNHEZRJJ7LvbC5k3+CQX'
minio_secure = False
db_host = '172.16.99.29'
db_port = 3306
db_user = 'root'
db_password = 'password'

# 通过global_config向sdk传入minio和db信息
client_config.minio_host = minio_host
client_config.minio_access_key = minio_access_key
client_config.minio_secret_key = minio_secret_key
client_config.minio_secure = minio_secure

client_config.db_host = db_host
client_config.db_port = db_port
client_config.db_user = db_user
client_config.db_password = db_password

# 注册自定义算法
register('my_alg', MyAlgorithm)
register('fake_alg', FakeAlgorithm)

# 如果有内置模型可以在这里指定模型id，会在服务启动时load起来
# set_preload_models('my_alg', ['pretrain_model_id1', 'pretrain_model_id2'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
