from __future__ import annotations

from typing import FrozenSet, Optional

import yaml


class KubeConfigBuilder:
    def __init__(self):
        self._state = {
            "apiVersion": "v1",
            "kind": "Config",
            "preferences": {},
            "clusters": [],
            "users": [],
            "contexts": [],
        }

    @property
    def all_clusters(self) -> FrozenSet[str]:
        return frozenset(cluster["name"] for cluster in self._state["clusters"])

    @property
    def all_users(self) -> FrozenSet[str]:
        return frozenset(user["name"] for user in self._state["users"])

    @property
    def all_contexts(self) -> FrozenSet[str]:
        return frozenset(context["name"] for context in self._state["contexts"])

    def add_cluster(
        self,
        cluster_name: str,
        cluster_ca: str,
        cluster_address: str,
    ) -> KubeConfigBuilder:
        if cluster_name in self.all_clusters:
            raise ValueError(f"Cluster name already exists: {cluster_name}")

        self._state["clusters"].append(
            {
                "cluster": {
                    "certificate-authority-data": cluster_ca,
                    "server": cluster_address,
                },
                "name": cluster_name,
            }
        )
        return self

    def add_user_eks(
        self,
        user_name: str,
        vault_token: str,
        vault_address: str,
        vault_ca_path: str,
        vault_path: str,
        vault_helper_path: Optional[str] = None,
    ) -> KubeConfigBuilder:
        if user_name in self.all_users:
            raise ValueError(f"User name already exists: {user_name}")

        self._state["users"].append(
            {
                "user": {
                    "exec": {
                        "apiVersion": "client.authentication.k8s.io/v1alpha1",
                        "args": [
                            "eks",
                            "--eks-cluster=bedrock",
                            "--eks-ttl=1h",
                            f"--vault-token={vault_token}",
                            f"--vault-address={vault_address}",
                            f"--vault-ca-cert={vault_ca_path}",
                            vault_path,
                        ],
                        "command": vault_helper_path or "/usr/bin/vault-k8s-helper",
                    }
                },
                "name": user_name,
            }
        )
        return self

    def add_user_eks_local(
        self,
        user_name: str,
        aws_cli_path: Optional[str] = None,
    ) -> KubeConfigBuilder:
        if user_name in self.all_users:
            raise ValueError(f"User name already exists: {user_name}")

        self._state["users"].append(
            {
                "user": {
                    "exec": {
                        "apiVersion": "client.authentication.k8s.io/v1alpha1",
                        "args": [
                            "--region",
                            "ap-southeast-1",
                            "eks",
                            "get-token",
                            "--cluster-name",
                            "bedrock",
                        ],
                        "command": aws_cli_path or "aws",
                        "provideClusterInfo": False,
                    }
                },
                "name": user_name,
            }
        )
        return self

    def add_user_gke(
        self,
        user_name: str,
        vault_token: str,
        vault_address: str,
        vault_ca_path: str,
        vault_path: str,
        vault_helper_path: Optional[str] = None,
    ) -> KubeConfigBuilder:
        if user_name in self.all_users:
            raise ValueError(f"User name already exists: {user_name}")

        self._state["users"].append(
            {
                "user": {
                    "auth-provider": {
                        "config": {
                            "cmd-args": " ".join(
                                [
                                    "gke",
                                    f"--vault-token={vault_token}",
                                    f"--vault-address={vault_address}",
                                    f"--vault-ca-cert={vault_ca_path}",
                                    vault_path,
                                ]
                            ),
                            "cmd-path": vault_helper_path or "/usr/bin/vault-k8s-helper",
                            "expiry-key": "{.token_expiry}",
                            "token-key": "{.token}",
                        },
                        "name": "gcp",
                    }
                },
                "name": user_name,
            }
        )
        return self

    def add_user_gke_local(
        self,
        user_name: str,
        gcloud_sdk_path: Optional[str] = None,
    ) -> KubeConfigBuilder:
        if user_name in self.all_users:
            raise ValueError(f"User name already exists: {user_name}")

        self._state["users"].append(
            {
                "user": {
                    "auth-provider": {
                        "config": {
                            "cmd-args": "config config-helper --format=json",
                            "cmd-path": gcloud_sdk_path or "/usr/lib/google-cloud-sdk/bin/gcloud",
                            "expiry-key": "{.credential.token_expiry}",
                            "token-key": "{.credential.access_token}",
                        },
                        "name": "gcp",
                    }
                },
                "name": user_name,
            }
        )
        return self

    def add_context(
        self,
        context_name: str,
        cluster_name: str,
        user_name: str,
        namespace: Optional[str] = None,
    ) -> KubeConfigBuilder:
        if context_name in self.all_contexts:
            raise ValueError(f"Context name already exists: {context_name}")
        if cluster_name not in self.all_clusters:
            raise ValueError(f"Cluster name not found: {cluster_name}")
        if user_name not in self.all_users:
            raise ValueError(f"User name not found: {user_name}")

        context = {
            "cluster": cluster_name,
            "user": user_name,
        }
        if namespace:
            context["namespace"] = namespace

        self._state["contexts"].append(
            {
                "context": context,
                "name": context_name,
            }
        )
        return self

    def set_current_context(self, context_name: str) -> KubeConfigBuilder:
        if context_name not in self.all_contexts:
            raise ValueError(f"Context name not found: {context_name}")

        self._state["current-context"] = context_name
        return self

    def dump(self, outfile) -> None:
        yaml.dump(self._state, outfile)

    def __str__(self):
        return yaml.safe_dump(self._state)
