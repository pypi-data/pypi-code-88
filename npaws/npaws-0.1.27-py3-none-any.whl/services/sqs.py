import json
from ..client import Boto3Client


class SQSClient(Boto3Client):
    """
    """
    
    def __init__(self):
        """
        """
        super().__init__('sqs')

    def send_preprocess_job(self,
                            project_id: int,
                            document_id: int):
        """
        """
        msg_body = {
            'projectId': project_id,
            'pageId': document_id
        }
        self.send_message(
            QueueUrl="https://sqs.eu-west-3.amazonaws.com/749868801319/preprocess-queue",
            MessageBody=json.dumps(msg_body)
        )
        
    def send_ocr_job(self,
                     project_id: int,
                     page_id: int):
        """
        """
        msg_body = {
            'projectId': project_id,
            'pageId': page_id
        }
        self.send_message(
            QueueUrl="https://sqs.eu-west-3.amazonaws.com/749868801319/ocr-queue",
            MessageBody=json.dumps(msg_body)
        )
