from typing import Dict, Optional


def get_kafka_output_topic_from_app_name(app_name: str, version: str) -> str:
    return f"{app_name}_{version}"


def get_confluent_config(
    brokers: str,
    prefix: str = "",
    api_key: Optional[str] = None,
    secret: Optional[str] = None,
) -> Dict[str, str]:
    config = {
        f"{prefix}bootstrap.servers": brokers,
        f"{prefix}security.protocol": "SASL_SSL",
        f"{prefix}sasl.mechanism": "PLAIN",
        f"{prefix}ssl.endpoint.identification.algorithm": "https",
    }
    if api_key is not None and secret is not None:
        config[f"{prefix}sasl.username"] = api_key
        config[f"{prefix}sasl.password"] = secret
    return config
