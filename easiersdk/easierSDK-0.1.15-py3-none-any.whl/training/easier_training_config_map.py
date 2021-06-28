config_map = """
apiVersion: v1
kind: ConfigMap
metadata:
  name: easier-training
data:
  easier_user: 
  easier_password: 
  repo: 
  category: 
  model_name: 
  experimentID: 
  data_path:
  TF_CONFIG:
"""

config_map_distributed = """
apiVersion: v1
kind: ConfigMap
metadata:
  name: easier-dist-training
data:
  easier_user: 
  easier_password: 
  repo: 
  category: 
  model_name: 
  experimentID: 
  data_path:
  TF_CONFIG:
"""