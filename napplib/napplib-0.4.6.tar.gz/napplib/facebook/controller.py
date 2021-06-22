import datetime
from pathlib import Path
from napplib.azure.blob_storage import BlobStorage

class FacebookController:
    @classmethod
    def send_to_storage(self, products, store_name, account_name, account_key, project, path):
        try:
            # write local xml
            dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            xml_path = Path(f'{dt}_products.xml').absolute()
            with xml_path.open('w', encoding='utf-8') as output:
                output.write(products)

            # Send orders to storage
            BlobStorage.upload_blob(
                account_name=account_name,
                account_key=account_key,
                path=path,
                project=project,
                store_name=store_name,
                output_file=str(xml_path)
            )
        except Exception as e:
            print(f'Failed to save payload as blob storage file. {e}')
