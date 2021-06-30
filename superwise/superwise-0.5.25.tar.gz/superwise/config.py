import os


class Config:
    FRONTEGG_URL = os.environ.get("FRONTEGG_SUPERWISE_URL", "https://superwise-prod.frontegg.com")
    SUPERWISE_HOST = os.environ.get("SUPERWISE_HOST", "api.superwise.ai")
    POOLING_INTERVAL_SEC = 15
