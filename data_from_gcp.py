import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../oddnary_storage_manager_key.json"


def list_files(bucket_name):
    """Lists all the files in the bucket."""
    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    # print(blobs)
    for blob in blobs:
        print(blob.name)
        # read_file(blob.name)


def read_file(file_name):
    """Reads the contents of a file."""
    storage_client = storage.Client()

    # Note: Client.get_bucket requires at least package version 1.17.0.
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)

    content = blob.download_as_text()
    # print(content)


bucket_name = 'oddnary-bucket'

# 버킷 이름을 사용하여 함수를 호출합니다.
a = list_files(bucket_name)
print(a)

# read_file(a)
