import boto3
from botocore.exceptions import ClientError


# To get list of buckets present in AWS using S3 client
def get_buckets_client():
    session = boto3.session.Session()
    # User can pass customized access key, secret_key and token as well
    s3_client = session.client("s3")
    response = s3_client.list_buckets()
    buckets = []
    for bucket in response["Buckets"]:
        buckets += {bucket["Name"]}
    return buckets


def get_fileNames():
    session = boto3.session.Session()
    # User can pass customized access key, secret_key and token as well
    s3_client = session.client("s3")
    response = s3_client.list_objects_v2(Bucket="vault-hunters")
    for content in response["Contents"]:
        s3_client.download_file("vault-hunters", content["Key"], "vault-hunters-new")


print(get_fileNames())
