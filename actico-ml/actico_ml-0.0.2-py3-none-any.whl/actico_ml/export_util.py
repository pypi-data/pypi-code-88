#  Copyright (c) ACTICO GmbH, Germany. All rights reserved.

import logging
import requests

def release_model(api_key, machine_learning_server_url, model_name, training_frame_name,
    module_id, project_id, version=None):

  params = {"trainingFrameName": training_frame_name,"moduleId": module_id, "projectId": project_id, "version": version,
            "pipelineName": None}

  is_successful = False

  try:
    r = requests.post(
        machine_learning_server_url + "/machine-learning/v1/models/" +
        model_name + "/release", headers={'Authorization': 'ApiKey '+api_key}, params=params)
    r.raise_for_status()
    if r.status_code == 200:
      is_successful = True
  except requests.exceptions.HTTPError as e:
    logging.warning(e.response.text)

  return is_successful

if __name__ == '__main__':
  release_model(api_key="QWRtaW5+ZGV2LXN0YXRpYy1rZXk=",machine_learning_server_url="http://localhost:8080", model_name="credit-rf-model",training_frame_name="credit-train.hex",module_id= "actico", project_id="credit-rf")
