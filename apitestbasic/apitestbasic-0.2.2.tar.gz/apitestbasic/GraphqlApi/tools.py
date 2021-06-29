from faker import Faker
from faker.providers import BaseProvider
import random
import logging
import time


class MyProvider(BaseProvider):
    fake = Faker(['zh_CN'])

    def code(self):
        return self.fake.currency_code() + str(self.fake.random_int())

    def model(self):
        return self.fake.word() + self.fake.gou()

    def title(self):
        return self.fake.text(20)

    def brief(self):
        return self.fake.text(100)

    def description(self):
        return self.fake.text(500)

    def content(self):
        return self.fake.text(100)

    def factory(self):
        return random.choice(["测试工厂", "外星人工厂", "能量工厂"])

    def category(self):
        return random.choice(["生产设备", "公共类设备", "辅助设备"])

    def purpose(self):
        return random.choice(["生产", "辅助", "加压"])

    def usingStatus(self):
        return random.choice(["使用中", "废弃中", "加载中"])

    def brand(self):
        return random.choice(["喜临门", "外星人", "罗技", "雷蛇"])

    def manufacturer(self):
        return random.choice(["中国上海英格索兰压缩机", "外星人", "罗技", "雷蛇"])

    def distributor(self):
        return random.choice(["经销商1", "经销商2", "经销商3"])

    def frequency(self):
        return random.choice(["一天一次", "一月一次", "三月一次"])


class MyFaker(object):

    def __init__(self, fake_map=None):
        # 如果要关联到已存在的规则使用fake_map
        self.fake_map = {}
        self.fake = Faker()
        self.fake.add_provider(MyProvider)

    def add_provider(self, provider: BaseProvider):
        self.fake.add_provider(provider)

    def add_fake_map(self, pos=None, **kwargs):
        if pos:
            self.fake_map.update(pos)
        self.fake_map.update(**kwargs)

    def create_string(self, param, **identity):
        name = param.param.real_name
        if getattr(self, name.lower()):
            return getattr(self, name.lower())
        if identity.get("is_random", False):
            str_len = identity.get("string_len", 5)
            return "_".join([name, create_num_string(str_len)])
        elif identity.get("num"):
            return "_".join([name, str(identity.get("num"))])
        else:
            return name

    def __getattr__(self, item):
        if item == "password":
            return self.fake.password(special_chars=False)
        try:
            return getattr(self.fake, item)()
        except AttributeError:
            try:
                return getattr(self.fake, self.fake_map[item])()
            except KeyError:
                logging.debug("fake_map 不存在 %s" % item)
            except AttributeError:
                logging.debug("fake_map %s 的对应不对" % item)
        return "_".join([item, create_num_string(5)])


fake = MyFaker()


def create_num_string(num, prefix=None):
    samples = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
               'e', 'd', 'c', 'b', 'a', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "_"]

    if prefix:
        return prefix + ''.join(random.sample(samples, num))
    return ''.join(random.sample(samples, num))


def create_timestamp(delay=0, before=0):
    return int(time.time() * 1000) + delay * 60 * 1000 - before * 60 * 1000
