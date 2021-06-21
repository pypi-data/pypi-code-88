# -*- coding:utf-8 -*-
"""
@desc: 
"""

RABBITMQ_CONNECTION_PARAMETERS = "amqp://guest:guest@localhost:5672/"
SCHEDULER_MAX_IDLE_TIME = 30  # 最大闲置时间
SPIDER_PARSE_FAILD_MAX_TIMES = 60  # 允许解析出错的最大次数
RABBITMQ_DURABLE = True  # 队列持久化
RABBITMQ_CONFIRM_DELIVERY = True  # 开启手动消息确认
HTTP_REQUEUE_STATUS = []
