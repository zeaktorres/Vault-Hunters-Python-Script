import boto3
from botocore.exceptions import ClientError

# To get list of buckets present in AWS using S3 client
def get_buckets_client():
   session = boto3.session.Session()
   # User can pass customized access key, secret_key and token as well
   s3_client = session.client('s3')
   try:
      response = s3_client.list_buckets()
      buckets =[]
   for bucket in response['Buckets']
      buckets += {bucket["Name"]}

      except ClientError:
         print("Couldn't get buckets.")
         raise
      else:
         return buckets
print(get_buckets_client())
