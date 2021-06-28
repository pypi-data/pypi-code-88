deployment = """
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: easier-serving
  name: pod-easier-serving
spec:
  replicas: 1
  selector:
    matchLabels:
      app: easier-serving
  template:
    metadata:
      labels:
        app: easier-serving
  containers:
  - name: easier-serving
    image: easierai/easier_model:latest
    imagePullPolicy: Always
    ports:
    - containerPort: 5000
    envFrom:
      - configMapRef:
          name: easier-serving
    resources:
      requests:
        memory: "512Mi"
        cpu: "0.5"
      limits:
        memory: "1024Mi"
        cpu: "1"
  restartPolicy: Always
  hostAliases:
  - ip: "213.227.145.163"
    hostnames:
    - "minio.test-easier-ai.eu"
  # imagePullSecrets:
  # - name: regcred
"""