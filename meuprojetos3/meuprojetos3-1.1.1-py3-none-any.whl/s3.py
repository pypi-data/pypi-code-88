import os
import urllib.request
from PIL import Image

import boto3 as boto3
from botocore.exceptions import ClientError


def conectar():
    access_key = 'AKIAZP3D4TZSAB6REDWO'
    access_secret = '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'
    return boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret
    )


def salvar_imagem(url: str):
    urllib.request.urlretrieve(url, 'fotos/imagem.jpg')


def converter_imagem_salva_e_informar_diretorio() -> str:
    imagem_para_converter = Image.open('fotos/imagem.jpg').convert("RGB")
    imagem_para_converter.save("convertidas/imagem.jpg", "jpeg")
    imagem_para_converter.close()
    return os.path.join(os.getcwd(), 'convertidas')


def subir_imagem_s3(url: str):
    bucket_name = 'fotos-da-pompeia'
    s3 = conectar()
    salvar_imagem(url)
    caminho_da_imagem_convertida = converter_imagem_salva_e_informar_diretorio()
    try:
        respe = s3.upload_file(os.path.join(caminho_da_imagem_convertida, "imagem.jpg"), bucket_name,
                               'anthony.jpg')
        return "https://fotos-da-pompeia.s3.amazonaws.com/foto-sg1.jpg"
    except ClientError as e:
        print(f'Credencial incorreta {e}')
    except Exception as e:
        print(f'erro {e}')
