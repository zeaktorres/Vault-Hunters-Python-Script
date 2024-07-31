import boto3
import subprocess


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
        "unzip -o world-new.zip",
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


getPreviousSave()
