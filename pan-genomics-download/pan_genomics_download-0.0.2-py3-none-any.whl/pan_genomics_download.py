import argparse
import logging
import requests
import os

from requests.api import patch

class pan_genomics_download(object):
    def __init__(self,url:str,target_path:str='.') -> None:
        self.shared_url=url
        self.headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 YaBrowser/21.5.2.638 Yowser/2.5 Safari/537.36"}
        self.target_path=target_path
        self.files=[]
        
        self.get_ShareEventId()
        self.get_file_list()

    def get_ShareEventId(self) -> None:
        url='https://pan.genomics.cn/ucdisk/api/2.0/share/link/shareLongUrl'
        data={'shortUrl':self.shared_url }
        shared_id_json=requests.post(url=url,data=data,headers=self.headers).json()
        self.share_event_id=shared_id_json['body']['bean']['id']

    def get_file_list(self) ->None:
        url='https://pan.genomics.cn/ucdisk/s/api/2.0/share/link/info'
        data={
            'shareEventId': self.share_event_id,
            'pageNumber': 1,
            'pageSize': 50,
            'code':'' 
        }

        node_id_json=requests.post(url=url,data=data,headers=self.headers).json()
        for item in node_id_json['body']['rows']:
            self.files.extend(self.process_row(item,self.target_path))

        logger.info('get files list successfully')


    def process_row(self,item:dict,target_path:str,files=[]) -> list:
        if not target_path:
            target_path=self.target_path
        
        if item['fileSize'] == 0:  # 文件夹
            url='https://pan.genomics.cn/ucdisk/api/2.0/share/link/rec/list/dir'
            data={
                'pageNumber': 1,
                'pageSize': 50,
                'keyword':'' ,
                'shareEventId': self.share_event_id,
                'nodeId': item['id'],
                'code': '',
            }
            
            list_dir_json=requests.post(url=url,data=data,headers=self.headers).json()
            for row in list_dir_json['body']['rows']:
                path=os.path.join(target_path,item['name'])
                self.process_row(row,path,files)
            
        else:  # 文件
            files.append({'id': item['id'], 'name': item['name'], 'target_path': os.path.join(target_path,  item['name'])})
            
        return files

    def filter_file_suffix(self,suffix) -> None:
        self.files=[file for file in self.files if file['name'].endswith(suffix)]
        logger.info(f'filter files list with suffix {suffix} successfully')

    def download(self,flat:bool=False) -> None:
        download_requests_urls=[f'https://pan.genomics.cn/ucdisk/api/2.0/share/link/download?shareEventId={self.share_event_id}&nodeId={file["id"]}&code=' for file in self.files ]
        
        if flat:
            targets=[os.path.join(self.target_path,file['name']) for file in self.files]
        else:
            targets=[file['target_path'] for file in self.files]


        for url,target in zip(download_requests_urls,targets):
            res=requests.get(url=url,headers=self.headers).content

            folder=os.path.dirname(target)
            os.makedirs(folder,exist_ok=True)

            with open (target,'wb') as fp:
                fp.write(res)

            logger.info(f'{target} download successfully')


def interface():
    """
    pan-genomics-download is a convinient way to download all files in a pan.genomics.cn share link.

    Returns:
        tuple: () 
    """
    parser = argparse.ArgumentParser(description="pan-genomics_download")
    parser.add_argument("-u",
                        "--url",
                        type=str,
                        required=True,
                        help="shared link")
    parser.add_argument("-o",
                        "--target_path",
                        type=str,
                        required=False,
                        default='.',
                        help="target path to store files")   
    parser.add_argument("-s",
                        "--suffix",
                        type=str,
                        required=False,
                        help="allowed file suffix")
    parser.add_argument("-f",
                        "--flat",
                        action='store_true',
                        default=False,                        
                        help="ignore the directory hierarchy  and download all files to target path directly")     

    args=parser.parse_args()


    # return unparsed args as a dict
    return args


def main():
    args = interface()

    pgd=pan_genomics_download(url=args.url,target_path=args.target_path)

    if args.suffix:
        pgd.filter_file_suffix(suffix=args.suffix)
    
    pgd.download(args.flat)


# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger.addHandler(sh)

if __name__ == "__main__":
    main()
