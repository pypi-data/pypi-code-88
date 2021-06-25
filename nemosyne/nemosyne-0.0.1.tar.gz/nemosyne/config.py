import os 
from dotenv import load_dotenv
load_dotenv()
access_key =os.getenv("access_key")
secret_key = os.getenv('secret_key')

endpoint = os.getenv('endpoint')

bucket_name = os.getenv("bucket_name")