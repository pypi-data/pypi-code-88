deployment = """
apiVersion: batch/v1
kind: Job
metadata:
  labels:
    app: easier-training
  name: job-easier-training
spec:
  backoffLimit: 0
  template:
    metadata:
      labels:
        app: easier-training
    spec:
      containers:
      - name: easier-training
        image: easierai/easier_training:latest
        imagePullPolicy: Always
        envFrom:
          - configMapRef:
              name: easier-training
        resources:
          requests:
            memory: "512Mi"
            cpu: "1"
          limits:
            memory: "2056Mi"
            cpu: "1.5"
      restartPolicy: Never
      hostAliases:
      - ip: "213.227.145.163"
        hostnames:
        - "minio.test-easier-ai.eu"
"""

deployment_distributed = """
apiVersion: batch/v1
kind: Job
metadata:
  labels:
    app: easier-dist-training
  name: job-easier-dist-training
spec:
  backoffLimit: 0
  template:
    metadata:
      labels:
        app: easier-dist-training
    spec:
      containers:
      - name: easier-dist-training
        image: easierai/easier_distributed_training:latest
        imagePullPolicy: Always
        envFrom:
          - configMapRef:
              name: easier-dist-training
        containerPort: 5010
        resources:
          requests:
            memory: "1024Mi"
            cpu: "1"
          limits:
            memory: "2056Mi"
            cpu: "1.5"
      restartPolicy: Never
      hostAliases:
      - ip: "213.227.145.163"
        hostnames:
        - "minio.test-easier-ai.eu"
"""

deployment_pod = """
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: easier-training
  name: pod-easier-training
spec:
  replicas: 1
  selector:
    matchLabels:
      app: easier-training
  template:
    metadata:
      labels:
        app: easier-training
  containers:
  - name: easier-training
    image: easierai/easier_training:1.0
    imagePullPolicy: Always
    envFrom:
      - configMapRef:
          name: easier-training
  restartPolicy: Never
"""

deployment_pvc = """
apiVersion: v1
kind: Job
metadata:
  labels:
    app: easier-training
  name: pod-easier-training
spec:
  replicas: 1
  selector:
    matchLabels:
      app: easier-training
  template:
    metadata:
      labels:
        app: easier-training
  volumes:
    - name: easier-training
      persistentVolumeClaim:
        claimName: easier-training-claim
  containers:
  - name: easier-training
    image: easierai/easier_training:1.0
    imagePullPolicy: Always
    envFrom:
      - configMapRef:
          name: easier-training
    volumeMounts:
      - mountPath: "/train"
        name: easier-training-claim
  restartPolicy: Always
  initContainers:
    - name: easier-training-load-data
      image: easierai/easier_training_load_data:1.0
      imagePullPolicy: Always
      envFrom:
      - configMapRef:
          name: easier-training
      volumeMounts:
        - mountPath: "/train"
          name: easier-training-claim
  # imagePullSecrets:
  # - name: regcred
"""