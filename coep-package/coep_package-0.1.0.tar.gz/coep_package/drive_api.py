from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from googleapiclient.discovery import build

def verifier(colab=True):
    if(colab==True):
        from google.colab import auth
        auth.authenticate_user()
        service = build('drive', 'v3')
    else:
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(os.path.dirname(__file__)+'/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('drive', 'v3', credentials=creds)
    return service
  

def delete( folder_id, file_name,colab=True):
    service = verifier(colab)
    if not folder_id:
        print('Parameter folder_id missing. Execution Stopped!')
        return

    if not file_name:
        print('Parameter file_name missing. Execution Stopped!')
        return

    try:
        results = service.files().list(q=f"name='{file_name}' and '{folder_id}' in parents", fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        old_file_id = items[0]['id']
    except:
        print("Error encountered, please check that the parameters provided are correct!")
        return

    deletedFile = service.files().delete(fileId=old_file_id).execute()
    if deletedFile == '':
        print(f"{file_name} deleted succesfully")
        return

def upload( folder_id, file_name, upload_name = '',colab=True):
    service = verifier(colab)
    if not folder_id:
        print('Parameter folder_id missing. Execution Stopped!')
        return

    if not file_name:
        print('Parameter file_name missing. Execution Stopped!')
        return

    try:
        file_metadata = {'name': upload_name if upload_name != '' else file_name, 'parents': [folder_id]}
        media = MediaFileUpload(file_name, mimetype='text/csv')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        if file.get('id') != '':
            print(f"{file_name} has been uploaded succesfully")
            return
    except:
        print("Error encountered, please check that the parameters provided are correct!")

def deleteAndUpload( folder_id, file_name, upload_name = '',colab=True):
    delete( folder_id, file_name,colab)
    upload( folder_id, file_name, upload_name,colab)