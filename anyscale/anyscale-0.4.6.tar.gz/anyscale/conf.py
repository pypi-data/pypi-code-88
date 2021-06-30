import os
from typing import Optional


AWS_PROFILE = None

ANYSCALE_ENDPOINTS = {
    "development": "https://anyscale-dev.dev",
    "staging": "https://anyscale.dev",
    "production": "https://beta.anyscale.com",
    "test": "",
}

if (
    "ANYSCALE_HOST" in os.environ
    and os.environ.get("ANYSCALE_HOST") not in ANYSCALE_ENDPOINTS.values()
):
    anyscale_env_default = "test"
else:
    anyscale_env_default = "production"

ANYSCALE_ENV = os.environ.get("DEPLOY_ENVIRONMENT", anyscale_env_default)
ANYSCALE_HOST = os.environ.get("ANYSCALE_HOST", ANYSCALE_ENDPOINTS[ANYSCALE_ENV])

# Global variable that contains the server session token.
CLI_TOKEN: Optional[str] = None

TEST_MODE = False
TEST_V2 = False

RAY_STATIC_GCS_PORT = 9031

ANYSCALE_IAM_ROLE_NAME = "anyscale-iam-role"
ANYSCALE_AWS_SECURITY_GROUP_NAME = "anyscale-security-group"

# The name of the default Anyscale shared k8s cloud.
ANYSCALE_K8S_CLOUD_NAME = "anyscale_k8s_cloud"
ANYSCALE_K8S_CLOUD_ID = "cld_41THJUKS3PBYvwIynRggIb"
