service = """
apiVersion: v1
kind: Service
metadata:
  name: service-easier-training
  labels:
    app: easier-training
spec:
  type: ClusterIP
  ports:
  - name: "5100"
    port: 5100
    targetPort: 5100
  selector:
    app: easier-training
"""

service_distributed = """
apiVersion: v1
kind: Service
metadata:
  name: service-easier-dist-training
  labels:
    app: easier-dist-training
spec:
  type: ClusterIP
  ports:
  - name: "6010"
    port: 6010
    targetPort: 6010
  - name: "6006"
    port: 6006
    targetPort: 6006
  selector:
    app: easier-dist-training
"""