"""
# cdk8s-mongo-sts

![Release](https://github.com/opencdk8s/cdk8s-mongo-sts/workflows/Release/badge.svg?branch=development)
[![npm version](https://badge.fury.io/js/cdk8s-mongo-sts.svg)](https://badge.fury.io/js/cdk8s-mongo-sts)
[![PyPI version](https://badge.fury.io/py/cdk8s-mongo-sts.svg)](https://badge.fury.io/py/cdk8s-mongo-sts)
![npm](https://img.shields.io/npm/dt/cdk8s-mongo-sts?label=npm&color=green)
![PyPi](https://img.shields.io/pypi/dm/cdk8s-mongo-sts?label=pypi&color=green)

Create a Replicated, Password protected MongoDB Statefulset on Kubernetes, powered by the [cdk8s project](https://cdk8s.io) 🚀

## Disclaimer

This construct is under heavy development, and breaking changes will be introduced very often. Please don't forget to version lock your code if you are using this construct.

## Overview

**cdk8s-mongo-sts** is a [cdk8s](https://cdk8s.io) library, and also uses [cvallance/mongo-k8s-sidecar](https://github.com/cvallance/mongo-k8s-sidecar) to manage the MongoDB replicaset.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
from constructs import Construct
from cdk8s import App, Chart, ChartProps
from cdk8s_mongo_sts import MyMongo

class MyChart(Chart):
    def __init__(self, scope, id, *, namespace=None, labels=None):
        super().__init__(scope, id, namespace=namespace, labels=labels)
        MyMongo(self, "dev",
            image="mongo",
            namespace="databases",
            default_replicas=3,
            volume_size="10Gi",
            create_storage_class=True,
            volume_provisioner="kubernetes.io/aws-ebs",
            storage_class_name="io1-slow",
            storage_class_params={
                "type": "io1",
                "fs_type": "ext4",
                "iops_per_gB": "10"
            },
            node_selector_params={
                "database": "dev"
            }
        )

app = App()
MyChart(app, "asd")
app.synth()
```

Create a secret for your DB that starts with the same name as your Statefulset with the following keys :

```
username
password
```

See [this](https://kubernetes.io/docs/concepts/configuration/secret/) for documentation on Kubernetes secrets.

Then the Kubernetes manifests created by `cdk8s synth` command will have Kubernetes resources such as `Statefulset`, `Service`, `ClusterRole`, `ClusterRoleBinding`, `ServiceAccount`, and `StorageClass` as follows.

<details>
<summary>manifest.k8s.yaml</summary>

```yaml
allowVolumeExpansion: true
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: io1-slow
parameters:
  fsType: ext4
  type: io1
  iopsPerGB: "10"
provisioner: kubernetes.io/aws-ebs
reclaimPolicy: Retain
---
apiVersion: v1
kind: Service
metadata:
  name: dev
  namespace: databases
spec:
  clusterIP: None
  ports:
    - port: 27017
      targetPort: 27017
  selector:
    db: dev
  type: ClusterIP
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: get-pods-role
  namespace: databases
rules:
  - apiGroups:
      - "*"
    resources:
      - pods
    verbs:
      - list
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: dev
  namespace: databases
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: dev
  namespace: databases
roleRef:
  apiGroup: ""
  kind: ClusterRole
  name: get-pods-role
subjects:
  - kind: ServiceAccount
    name: dev
    namespace: databases
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: dev
  namespace: databases
spec:
  replicas: 3
  selector:
    matchLabels:
      db: dev
  serviceName: dev
  template:
    metadata:
      labels:
        db: dev
    spec:
      containers:
        - env:
            - name: MONGO_SIDECAR_POD_LABELS
              value: db=dev
            - name: KUBE_NAMESPACE
              value: databases
            - name: MONGODB_DATABASE
              value: admin
            - name: MONGODB_USERNAME
              valueFrom:
                secretKeyRef:
                  key: username
                  name: dev
            - name: MONGODB_PASSWORD
              valueFrom:
                secretKeyRef:
                  key: password
                  name: dev
          image: cvallance/mongo-k8s-sidecar
          name: mongo-sidecar
        - args:
            - --replSet
            - rs0
            - --bind_ip
            - 0.0.0.0
            - --dbpath
            - /data/db
            - --oplogSize
            - "128"
          env:
            - name: MONGO_INITDB_ROOT_USERNAME
              valueFrom:
                secretKeyRef:
                  key: username
                  name: dev
            - name: MONGO_INITDB_ROOT_PASSWORD
              valueFrom:
                secretKeyRef:
                  key: password
                  name: dev
          image: mongo
          name: dev
          ports:
            - containerPort: 27017
          resources:
            limits:
              cpu: 400m
              memory: 512Mi
            requests:
              cpu: 200m
              memory: 256Mi
          volumeMounts:
            - mountPath: /data/db
              name: dev
      nodeSelector:
        database: dev
      securityContext:
        fsGroup: 999
        runAsGroup: 999
        runAsUser: 999
      serviceAccountName: dev
      terminationGracePeriodSeconds: 10
  volumeClaimTemplates:
    - metadata:
        name: dev
      spec:
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
        storageClassName: io1-slow
```

</details>

## Installation

### TypeScript

Use `npm` or `yarn` to install.

```shell
$ npm install -s cdk8s-mongo-sts
```

or

```shell
$ yarn add cdk8s-mongo-sts
```

### Python

```shell
$ pip install cdk8s-mongo-sts
```

## Contribution

1. Fork ([https://github.com/Hunter-Thompson/cdk8s-mongo-sts/fork](https://github.com/Hunter-Thompson/cdk8s-mongo-sts/fork))
2. Bootstrap the repo:

   ```bash
   npx projen   # generates package.json
   yarn install # installs dependencies
   ```
3. Development scripts:
   |Command|Description
   |-|-
   |`yarn compile`|Compiles typescript => javascript
   |`yarn watch`|Watch & compile
   |`yarn test`|Run unit test & linter through jest
   |`yarn test -u`|Update jest snapshots
   |`yarn run package`|Creates a `dist` with packages for all languages.
   |`yarn build`|Compile + test + package
   |`yarn bump`|Bump version (with changelog) based on [conventional commits]
   |`yarn release`|Bump + push to `master`
4. Create a feature branch
5. Commit your changes
6. Rebase your local changes against the master branch
7. Create a new Pull Request (use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for the title please)

## Licence

[Apache License, Version 2.0](./LICENSE)

## Author

[Hunter-Thompson](https://github.com/Hunter-Thompson)
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from ._jsii import *

import constructs


class MyMongo(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@opencdk8s/cdk8s-mongo-sts.MyMongo",
):
    """(experimental) MongoDB Stateful Set class.

    :stability: experimental
    """

    def __init__(
        self,
        scope: constructs.Construct,
        name: builtins.str,
        *,
        image: builtins.str,
        create_storage_class: typing.Optional[builtins.bool] = None,
        default_replicas: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_selector_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        resources: typing.Optional["ResourceRequirements"] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        storage_class_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        volume_provisioner: typing.Optional[builtins.str] = None,
        volume_size: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param scope: -
        :param name: -
        :param image: (experimental) The Docker image to use for this app.
        :param create_storage_class: (experimental) Option to create storage class, if enabled, a storage class will be created for the statefulset. Default: true
        :param default_replicas: (experimental) Number of replicas. Default: 3
        :param namespace: (experimental) The Kubernetes namespace where this app to be deployed. Default: 'default'
        :param node_selector_params: (experimental) nodeSelector params. Default: - undefined
        :param resources: (experimental) Resources requests for the DB. Default: - Requests = { CPU = 200m, Mem = 256Mi }, Limits = { CPU = 400m, Mem = 512Mi }
        :param storage_class_name: (experimental) The storage class to use for our PVC. Default: 'gp2-expandable'
        :param storage_class_params: (experimental) Storage class params. Default: - { type = gp2, fsType: ext4 }
        :param volume_provisioner: (experimental) Each StorageClass has a provisioner that determines what volume plugin is used for provisioning PVs. This field must be specified. See `this <https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner>`_ for Ref Default: 'kubernetes.io/aws-ebs'
        :param volume_size: (experimental) The Volume size of our DB in string, e.g 10Gi, 20Gi.

        :stability: experimental
        """
        opts = STSOptions(
            image=image,
            create_storage_class=create_storage_class,
            default_replicas=default_replicas,
            namespace=namespace,
            node_selector_params=node_selector_params,
            resources=resources,
            storage_class_name=storage_class_name,
            storage_class_params=storage_class_params,
            volume_provisioner=volume_provisioner,
            volume_size=volume_size,
        )

        jsii.create(MyMongo, self, [scope, name, opts])

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        """
        :stability: experimental
        """
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property # type: ignore[misc]
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        """
        :stability: experimental
        """
        return typing.cast(builtins.str, jsii.get(self, "namespace"))


@jsii.data_type(
    jsii_type="@opencdk8s/cdk8s-mongo-sts.ResourceQuantity",
    jsii_struct_bases=[],
    name_mapping={"cpu": "cpu", "memory": "memory"},
)
class ResourceQuantity:
    def __init__(
        self,
        *,
        cpu: typing.Optional[builtins.str] = None,
        memory: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param cpu: Default: - no limit
        :param memory: Default: - no limit

        :stability: experimental
        """
        self._values: typing.Dict[str, typing.Any] = {}
        if cpu is not None:
            self._values["cpu"] = cpu
        if memory is not None:
            self._values["memory"] = memory

    @builtins.property
    def cpu(self) -> typing.Optional[builtins.str]:
        """
        :default: - no limit

        :stability: experimental
        """
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory(self) -> typing.Optional[builtins.str]:
        """
        :default: - no limit

        :stability: experimental
        """
        result = self._values.get("memory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceQuantity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@opencdk8s/cdk8s-mongo-sts.ResourceRequirements",
    jsii_struct_bases=[],
    name_mapping={"limits": "limits", "requests": "requests"},
)
class ResourceRequirements:
    def __init__(
        self,
        *,
        limits: typing.Optional[ResourceQuantity] = None,
        requests: typing.Optional[ResourceQuantity] = None,
    ) -> None:
        """
        :param limits: (experimental) Maximum resources for the web app. Default: - CPU = 400m, Mem = 512Mi
        :param requests: (experimental) Required resources for the web app. Default: - CPU = 200m, Mem = 256Mi

        :stability: experimental
        """
        if isinstance(limits, dict):
            limits = ResourceQuantity(**limits)
        if isinstance(requests, dict):
            requests = ResourceQuantity(**requests)
        self._values: typing.Dict[str, typing.Any] = {}
        if limits is not None:
            self._values["limits"] = limits
        if requests is not None:
            self._values["requests"] = requests

    @builtins.property
    def limits(self) -> typing.Optional[ResourceQuantity]:
        """(experimental) Maximum resources for the web app.

        :default: - CPU = 400m, Mem = 512Mi

        :stability: experimental
        """
        result = self._values.get("limits")
        return typing.cast(typing.Optional[ResourceQuantity], result)

    @builtins.property
    def requests(self) -> typing.Optional[ResourceQuantity]:
        """(experimental) Required resources for the web app.

        :default: - CPU = 200m, Mem = 256Mi

        :stability: experimental
        """
        result = self._values.get("requests")
        return typing.cast(typing.Optional[ResourceQuantity], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceRequirements(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@opencdk8s/cdk8s-mongo-sts.STSOptions",
    jsii_struct_bases=[],
    name_mapping={
        "image": "image",
        "create_storage_class": "createStorageClass",
        "default_replicas": "defaultReplicas",
        "namespace": "namespace",
        "node_selector_params": "nodeSelectorParams",
        "resources": "resources",
        "storage_class_name": "storageClassName",
        "storage_class_params": "storageClassParams",
        "volume_provisioner": "volumeProvisioner",
        "volume_size": "volumeSize",
    },
)
class STSOptions:
    def __init__(
        self,
        *,
        image: builtins.str,
        create_storage_class: typing.Optional[builtins.bool] = None,
        default_replicas: typing.Optional[jsii.Number] = None,
        namespace: typing.Optional[builtins.str] = None,
        node_selector_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        resources: typing.Optional[ResourceRequirements] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        storage_class_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        volume_provisioner: typing.Optional[builtins.str] = None,
        volume_size: typing.Optional[builtins.str] = None,
    ) -> None:
        """
        :param image: (experimental) The Docker image to use for this app.
        :param create_storage_class: (experimental) Option to create storage class, if enabled, a storage class will be created for the statefulset. Default: true
        :param default_replicas: (experimental) Number of replicas. Default: 3
        :param namespace: (experimental) The Kubernetes namespace where this app to be deployed. Default: 'default'
        :param node_selector_params: (experimental) nodeSelector params. Default: - undefined
        :param resources: (experimental) Resources requests for the DB. Default: - Requests = { CPU = 200m, Mem = 256Mi }, Limits = { CPU = 400m, Mem = 512Mi }
        :param storage_class_name: (experimental) The storage class to use for our PVC. Default: 'gp2-expandable'
        :param storage_class_params: (experimental) Storage class params. Default: - { type = gp2, fsType: ext4 }
        :param volume_provisioner: (experimental) Each StorageClass has a provisioner that determines what volume plugin is used for provisioning PVs. This field must be specified. See `this <https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner>`_ for Ref Default: 'kubernetes.io/aws-ebs'
        :param volume_size: (experimental) The Volume size of our DB in string, e.g 10Gi, 20Gi.

        :stability: experimental
        """
        if isinstance(resources, dict):
            resources = ResourceRequirements(**resources)
        self._values: typing.Dict[str, typing.Any] = {
            "image": image,
        }
        if create_storage_class is not None:
            self._values["create_storage_class"] = create_storage_class
        if default_replicas is not None:
            self._values["default_replicas"] = default_replicas
        if namespace is not None:
            self._values["namespace"] = namespace
        if node_selector_params is not None:
            self._values["node_selector_params"] = node_selector_params
        if resources is not None:
            self._values["resources"] = resources
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if storage_class_params is not None:
            self._values["storage_class_params"] = storage_class_params
        if volume_provisioner is not None:
            self._values["volume_provisioner"] = volume_provisioner
        if volume_size is not None:
            self._values["volume_size"] = volume_size

    @builtins.property
    def image(self) -> builtins.str:
        """(experimental) The Docker image to use for this app.

        :stability: experimental
        """
        result = self._values.get("image")
        assert result is not None, "Required property 'image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def create_storage_class(self) -> typing.Optional[builtins.bool]:
        """(experimental) Option to create storage class, if enabled, a storage class will be created for the statefulset.

        :default: true

        :stability: experimental
        """
        result = self._values.get("create_storage_class")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def default_replicas(self) -> typing.Optional[jsii.Number]:
        """(experimental) Number of replicas.

        :default: 3

        :stability: experimental
        """
        result = self._values.get("default_replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        """(experimental) The Kubernetes namespace where this app to be deployed.

        :default: 'default'

        :stability: experimental
        """
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_selector_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) nodeSelector params.

        :default: - undefined

        :stability: experimental
        """
        result = self._values.get("node_selector_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def resources(self) -> typing.Optional[ResourceRequirements]:
        """(experimental) Resources requests for the DB.

        :default: - Requests = { CPU = 200m, Mem = 256Mi }, Limits = { CPU = 400m, Mem = 512Mi }

        :stability: experimental
        """
        result = self._values.get("resources")
        return typing.cast(typing.Optional[ResourceRequirements], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        """(experimental) The storage class to use for our PVC.

        :default: 'gp2-expandable'

        :stability: experimental
        """
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        """(experimental) Storage class params.

        :default: - { type = gp2, fsType: ext4 }

        :stability: experimental
        """
        result = self._values.get("storage_class_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def volume_provisioner(self) -> typing.Optional[builtins.str]:
        """(experimental) Each StorageClass has a provisioner that determines what volume plugin is used for provisioning PVs.

        This field must be specified.
        See `this <https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner>`_ for Ref

        :default: 'kubernetes.io/aws-ebs'

        :stability: experimental
        """
        result = self._values.get("volume_provisioner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[builtins.str]:
        """(experimental) The Volume size of our DB in string, e.g 10Gi, 20Gi.

        :stability: experimental
        """
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "STSOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MyMongo",
    "ResourceQuantity",
    "ResourceRequirements",
    "STSOptions",
]

publication.publish()
