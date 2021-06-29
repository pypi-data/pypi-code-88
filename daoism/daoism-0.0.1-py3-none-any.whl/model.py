class BaseAPIModel:
    API: str
    config: dict


class TransModel(BaseAPIModel):
    API = "https://openapi.youdao.com/api/"
    config = {"from": "auto", "to": "auto", "vocabId": ""}


class OcrModel(BaseAPIModel):
    API = "https://openapi.youdao.com/ocrapi"
    config = {
        "detectType": "10012",
        "langType": "auto",
        "imageType": "1",
        "docType": "json",
    }
