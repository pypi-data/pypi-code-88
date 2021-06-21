from ..client import (
    Boto3Client
)


class BatchClient(Boto3Client):
    """
    """
    
    def __init__(self):
        """
        """
        super().__init__('batch')
