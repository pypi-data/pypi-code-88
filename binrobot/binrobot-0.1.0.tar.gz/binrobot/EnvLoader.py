import os
from dotenv import load_dotenv


class EnvLoader:
    """ Загрузчик переменных среды """

    _was_inited = False

    _var_names = {
        "BINANCE_API_KEY",
        "BINANCE_API_SECRET",
        "TICKET",
        'LOG_STDOUT',
        'LOG_FILE',
        'LOG_TRADES',
        'ERROR_TO_TELEGRAM',
        "TELEGRAM_TOKEN",
        "TELEGRAM_CHANNEL",
    }

    _variables = {}

    @classmethod
    def add_env_vars(cls, var_names: set):
        cls._var_names = cls._var_names.union(var_names)

    @classmethod
    def get_variables(cls):
        """ Получить переменные среды """
        if cls._was_inited is False:
            env_path = (os.path.join(os.path.abspath(os.curdir), '.env'))
            load_dotenv(env_path)

            for var_name in cls._var_names:
                value = os.getenv(var_name)
                if value is None:
                    raise AttributeError("Не установлено значение для обязательной перемнной среды " + var_name)
                cls._variables[var_name] = value

        return cls._variables

    @classmethod
    def get_var(cls, name: str):
        return cls.get_variables()[name]

    @classmethod
    def get_api_key(cls):
        return cls.get_variables()['BINANCE_API_KEY']

    @classmethod
    def get_api_secret(cls):
        return cls.get_variables()['BINANCE_API_SECRET']
