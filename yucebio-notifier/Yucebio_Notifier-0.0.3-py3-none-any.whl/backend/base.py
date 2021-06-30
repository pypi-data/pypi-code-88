import abc
from yucebio_config import Config

class BaseNotifier(object):
    config = Config('notifier')

    @abc.abstractmethod
    def send_message(self, user: str, title: str, markdown: str = None):
        """发送消息

        Args:
            user (str): 消息接受人员，如邮件接收人，钉钉员工号，钉钉群号
            title (str): 消息主题 或 一句话消息正文
            markdown (str, optional): Markdown格式的消息正文. Defaults to None.
        """
        raise NotImplementedError