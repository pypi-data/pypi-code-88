from yucebio_notifier.backend.dingding import DingAPI, RobotAPI, BaseNotifier

SUPPORTED_BACKENDS = {
    "dingding": DingAPI,
    "robot": RobotAPI
}

class Notifier(object):

    def __init__(self, backend: str = 'dingding'):
        if backend not in SUPPORTED_BACKENDS:
            raise RuntimeError(f"not supported backend! please use {list(SUPPORTED_BACKENDS)}")

        self.backend = backend
        self.api: BaseNotifier = SUPPORTED_BACKENDS[backend].getAPI()

    def send_message(self, user: str, title: str, markdown: str = None):
        """使用指定backend发送通知消息

        Args:
            user (str): 消息接受，若支持多个接受人员，需要使用逗号分隔
            title (str): 消息主题 或 一句话消息内容
            markdown (str, optional): Markdown格式的消息正文. Defaults to None.

        Returns:
            str: backend自定义内容
        """
        return self.api.send_message(user, title, markdown)