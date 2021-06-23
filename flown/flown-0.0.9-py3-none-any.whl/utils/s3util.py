from urllib.parse import urlparse, ParseResult
import boto3

s3 = boto3.client('s3')


def s3uri_to_console_url(s3uri: str, is_obj: bool):
    s3uri_obj: ParseResult = urlparse(s3uri)
    bucket_name = s3uri_obj.netloc  # 'bucket.suntory.sic.project-2501'
    region_name = 'us-east-1'
    prefix = s3uri_obj.path[1:] + ('' if is_obj else '/')
    return f"https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}" \
           f"?region={region_name}" \
           f"&prefix={prefix}" \
           f"&showversions=false"


def s3uri_to_signed_get_url(s3uri: str):
    s3uri_obj: ParseResult = urlparse(s3uri)
    bucket = s3uri_obj.netloc
    key = s3uri_obj.path[1:]
    return s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=3600,
        HttpMethod='GET')
