"""
简单封装apscheduler，使用默认的executor和scheduler，通过传入单一的store参数来己简化任务调度系统使用

使用时需要先安装 apscheduler
"""

from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from yucebio_config import Config


class YucebioScheduler(object):
    """封装APScheduler，统一管理配置项
    """
    def __init__(self, prefix: str='yucebioscheduler', uri: str = None):
        self.store_name = None
        self._config = Config('scheduler')
        if uri:
            self.set_jobstore(prefix, uri)
        

    @property
    def config(self):
        return self._config

    def set_jobstore(self, store_name: str, uri: str):
        self.store_name = store_name
        self._config[store_name] = self._parse_uri(uri)
        self._config.reload()

    def create_scheduler(self, daemon=True):
        if not self.store_name or self.store_name not in self.config:
            raise RuntimeError("could not find the job store configure") 

        jobstores = self.config[self.store_name]

        self.scheduler = (BackgroundScheduler if daemon else BlockingScheduler)()
        self.scheduler.configure(
            jobstores={'default': jobstores},
            
        )
        return self.scheduler

    def _parse_uri(self, uri: str):
        """解析数据库URI，遵循 RFC-1738标准，dialect+driver://username:password@host:port/database

        1. 关系型数据库： SQLAlchemy
        2. mongo
        3. redis
        """
        prefix = uri.split(':')[0]
        dialect = prefix.split('+')[0]

        SQLALCHEMY_DIALECTS = ['sqlite', 'mysql', 'postgresql', 'oracle', 'mssql']
        if dialect in SQLALCHEMY_DIALECTS:
            return {"type": 'sqlalchemy', "url": uri}

        # database=mongo.db.name, collection="aps_jobs"
        MONGO_DIALECTS = ['mongodb']
        if dialect in MONGO_DIALECTS:
            return self._parse_mongo_uri(uri)

        # redis://root:xxxx@47.110.xx.xx:6379
        REDIS_DIALECTS = ['redis']
        if dialect in MONGO_DIALECTS:
            return self._parse_redis_uri(uri=uri)

        raise RuntimeError("无法解析URL，请使用mongodb或sqlalchey支持的数据库地址")

    def _parse_redis_uri(self, uri: str):
        """解析redis uri"""        
        tmp = str(uri)
        # 先去掉固定前缀
        if 'redis://' not in tmp:
            raise RuntimeError("无效URI，请使用 redis://[user[:pwd]@]host[:port]")
        tmp = tmp[8:]
        options = {'type': 'redis'}
        if '@' in tmp:
            profile, tmp = tmp.split('@')
            options['username'] = profile
            if ':' in profile:
                options['username'], options['password'] = profile.split(':')
        options['host'] = tmp
        if ':' in tmp:
            options['host'], options['port'] = tmp.split(':')
        return options

    def _parse_mongo_uri(self, uri: str):
        """解析mongodb协议 
        mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
        """
        tmp = str(uri)
        # 先去掉固定前缀
        if 'mongodb://' not in tmp:
            raise RuntimeError("无效URI，请使用 redis://[user[:pwd]@]host[:port]")
        tmp = tmp[10:]
        options = {'type': 'mongodb', "host": uri}
        # 提取出database参数
        if '/' in tmp:
            _, database = tmp.split('/')
            database = database.split('?')[0]
            if database:
                options['database'] = database
        return options



if __name__ == '__main__':
    ys = YucebioScheduler()

    ys.set_jobstore(store_type="default", store='sqlite:///jobs.sqlite')
    scheduler = ys.create_scheduler(daemon=False)
    scheduler.start()

    # TODO: 将当前进程放到后台
    while True:
        pass