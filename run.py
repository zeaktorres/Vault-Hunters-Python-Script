import boto3
import time
import subprocess
from botocore.exceptions import ClientError


def getPreviousSave():
    print("here")
    session = boto3.session.Session()
    # User can pass customized access key, secret_key and token as well
    s3_client = session.client("s3")
    s3_client.list_objects_v2(Bucket="vault-hunters")
    s3_client.download_file("vault-hunters", "world-new.zip", "world-new.zip")
    s3_client.download_file(
        "vault-hunters",
        "Vault-Hunters-3rd-Edition-3.14.3-server-files.zip",
        "Vault-Hunters-3rd-Edition-3.14.3-server-files.zip",
    )

    process = subprocess.Popen(
        "unzip -o Vault-Hunters-3rd-Edition-3.14.3-server-files.zip",
        shell=True,
        text=True,
    )
    print(process.stdout)
    process.wait()

    process = subprocess.Popen(
        "cp world-new.zip world-old.zip", shell=True, stdout=subprocess.PIPE
    )
    process.wait()

    process = subprocess.Popen(
        "echo 'eula=true' > eula.txt", shell=True, stdout=subprocess.PIPE
    )
    process.wait()


def uploadSave():
    session = boto3.session.Session()
    s3_client = session.client("s3")
    process = subprocess.Popen("rm world-old.zip", shell=True, stdout=subprocess.PIPE)
    process.wait()

    # Zip current world
    process = subprocess.Popen(
        "zip -r world-new.zip world", shell=True, stdout=subprocess.PIPE
    )
    process.wait()

    process = subprocess.Popen(
        "mv world-new.zip world-old.zip", shell=True, stdout=subprocess.PIPE
    )
    process.wait()

    # User can pass customized access key, secret_key and token as well
    s3_client.upload_file("world-new.zip", "vault-hunters", "world-new.zip")
    s3_client.upload_file("world-old.zip", "vault-hunters", "world-old.zip")


def startServer():
    subprocess.Popen(
        "java -Xmx3072M -Xms3072M -jar server.jar nogui pause", shell=True, text=True
    )


getPreviousSave()
startServer()
while True:
    uploadSave()
    time.sleep(15 * 60)
