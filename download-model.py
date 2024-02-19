import json
import boto3

def download_s3():
    # Replace with your own values
    bucket_name = "siri-model-registry"
    download_path = "local/path/to/save/file.txt"  # Local path to save the downloaded file
    
    # Create an S3 client
    s3 = boto3.client("s3")
    
    # Download the file
    try:
        s3.download_file(bucket_name, file_key, download_path)
        print("File downloaded successfully!")
    except Exception as e:
        print(f"Error downloading file: {e}")


def lambda_handler(event, context):
    # TODO implement
    _=download_s3()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
