from yucebio_uploader.ali import Uploader as AliUploader, BaseUploader

SupportedPlatforms = {
    'ali': AliUploader
}
SupportedPlatformNames = ['ali'] + AliUploader.ALIAS_NAME

def create_uploader(platform: str = 'ali') -> BaseUploader:
    if platform in SupportedPlatforms:
        return SupportedPlatforms[platform]()

    for cls in SupportedPlatforms.values():
        if platform in cls.ALIAS_NAME:
            return cls()
    raise RuntimeError(f"only support {list(SupportedPlatforms)}! please mail the Author!")
