from ..management.types import ManagementClientOptions
from ..management.authing import ManagementClient
from dotenv import load_dotenv
import os
load_dotenv()

management = ManagementClient(ManagementClientOptions(
    user_pool_id=os.getenv('APPROW_USERPOOL_ID'),
    secret=os.getenv('APPROW_USERPOOL_SECRET'),
    host=os.getenv('APPROW_SERVER')
))
