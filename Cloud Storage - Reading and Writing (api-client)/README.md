# Cloud Storage - Reading and Writing (api-client)

This application creates a test file, upload it to a bucket, prints details of all the files in the bucket and delete the text file created.

## Issues

- Install google-api-python-client
pip install --upgrade google-api-python-client
pip install -t lib google-api-python-client
pip install --force-reinstall google-api-python-client

- Update appengine_config.py to python packages folder
vendor.add('C:\Anaconda2\Lib\site-packages')

- ValueError: Credentials from google.auth specified, but google-api-python-client is unable to use these credentials unless google-auth-httplib2 is installed. Please install google-auth-httplib2.
pip install google-auth-httplib2

## Source
- https://github.com/GoogleCloudPlatform/python-docs-samples/tree/master/appengine/standard/storage/api-client

## Setup

Before running the sample:

1. You need a Cloud Storage Bucket. You create one with [`gsutil`](https://cloud.google.com/storage/docs/gsutil):

        gsutil mb gs://your-bucket-name

2. Update `main.py` and replace `<your-bucket-name>` with your Cloud Storage bucket.
