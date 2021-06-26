from slai.clients.gdrive import get_google_drive_client


class DriveClient:
    def __init__(self):
        self.client = get_google_drive_client()

    def upload_model_notebook(
        self, model_name, model_google_drive_folder_id, notebook_path, file_id=None
    ):
        model_notebook_google_drive_file_id = self.client.upload_file(
            filename=f"{model_name}.ipynb",
            local_path=notebook_path,
            parent_ids=[
                model_google_drive_folder_id,
            ],
            file_id=file_id,
        )

        return model_notebook_google_drive_file_id

    def download_latest_model_notebook(
        self, local_path, model_notebook_google_drive_file_id
    ):
        self.client.download_file(
            file_id=model_notebook_google_drive_file_id,
            local_path=local_path,
        )

    def create_model_folder(self, model_name, project_google_drive_folder_id):
        model_google_drive_folder_id = self.client.create_folder(
            name=f"{model_name}",
            parent_ids=[project_google_drive_folder_id],
        )
        return model_google_drive_folder_id

    def create_project_folder(self, folder_name):
        project_folder_google_drive_id = self.client.create_folder(
            name=f"{folder_name}",
            parent_ids=[],
        )
        return project_folder_google_drive_id
