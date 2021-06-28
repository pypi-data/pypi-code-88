ingress = """
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: ingress-easier-training
  kubernetes.io/ingress.allow-http: "true"
  nginx.ingress.kubernetes.io/backend-protocol: HTTP
  nginx.ingress.kubernetes.io/secure-backends: "false"
  labels:
    app: easier-training
spec:
  tls:
  - secretName: wildcard-easier-ai.eu
  rules:
  - host: easier-ai.eu
    http:
      paths:
      - backend:
          serviceName: service-easier-training
          servicePort: 5100
"""

ingress_dist = """
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: ingress-easier-dist-training
  kubernetes.io/ingress.allow-http: "true"
  nginx.ingress.kubernetes.io/backend-protocol: HTTP
  nginx.ingress.kubernetes.io/secure-backends: "false"
  labels:
    app: easier-dist-training
spec:
  tls:
  - secretName: wildcard-easier-ai.eu
  rules:
  - host: easier-ai.eu
    http:
      paths:
      - backend:
          serviceName: service-easier-dist-training
          servicePort: 6006
"""


ingress_dist_v1 = """
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-easier-dist-training
  # kubernetes.io/ingress.allow-http: "true"
  # nginx.ingress.kubernetes.io/backend-protocol: HTTP
  # nginx.ingress.kubernetes.io/secure-backends: "false"
  labels:
    app: easier-dist-training
spec:
  tls:
  - secretName: wildcard-easier-ai.eu
  rules:
  - host: easier-ai.eu
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: service-easier-dist-training
            port: 
              number: 6006
"""