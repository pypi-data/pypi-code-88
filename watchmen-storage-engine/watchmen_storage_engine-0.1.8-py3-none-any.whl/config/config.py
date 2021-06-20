import secrets
from typing import List, Dict, Any, Optional

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = ""
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    HOST_URL = "http://localhost:8000"
    ALGORITHM = "HS256"
    STORAGE_ENGINE = "mongo"
    PROJECT_NAME: str
    MONGO_SCHEMA = "watchmen"
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    MONGO_USERNAME: str = None
    MONGO_PASSWORD: str = None
    PRESTO_HTTP_URL = "http://localhost:8080"
    PRESTO_HOST: str = None
    PRESTO_PORT: int = None
    PRESTO_USER = "the_user"
    PRESTO_CATALOG = "mongo"
    PRESTO_SCHEMA = "watchmen"

    MYSQL_HOST: str = ""
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_DATABASE: str = 'watchmen'
    MYSQL_POOL_MAXCONNECTIONS: int = 6
    MYSQL_POOL_MINCACHED = 2
    MYSQL_POOL_MAXCACHED = 5

    ORACLE_LIB_DIR: str = ""
    ORACLE_HOST: str = ""
    ORACLE_PORT: int = 1521
    ORACLE_USER: str = ""
    ORACLE_PASSWORD: str = ""
    ORACLE_SERVICE: str = "XE"

    CONNECTOR_KAFKA = False
    KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
    KAFKA_TOPICS = ""

    NOTIFIER_PROVIDER = "email"
    EMAILS_ENABLED: bool = False
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = None
    EMAILS_TO: Optional[str] = None
    TOPIC_DATE_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
    DECIMAL = "decimal(32,2)"

    @validator("STORAGE_ENGINE", pre=True)
    def get_emails_enabled(cls, v: str, values: Dict[str, Any]) -> bool:
        # print(v)
        if v and v == "mongo":
            result = bool(
                values.get("MONGO_HOST")
                and values.get("MONGO_PORT"))
            if not result:
                raise ValueError("STORAGE_ENGINE dependency check MONGO_HOST and MONGO_PORT")
            else:
                return v
        elif v == "mysql":
            result = bool(
                values.get("MYSQL_HOST")
                and values.get("MYSQL_PORT")
                and values.get("MYSQL_USER")
            )
            if not result:
                raise ValueError("STORAGE_ENGINE dependency check MYSQL_HOST and MYSQL_PORT and MYSQL_USER")
            else:
                return v
        elif v == "oracle":
            result = bool(
                values.get("ORACLE_HOST")
                and values.get("ORACLE_PORT")
                and values.get("ORACLE_USER")
                and values.get("ORACLE_LIB_DIR")
                and values.get("ORACLE_SERVICE")
            )
            if not result:
                raise ValueError("STORAGE_ENGINE dependency check ORACLE_HOST and ORACLE_PORT and ORACLE_USER")
            else:
                return v

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True


settings = Settings()
