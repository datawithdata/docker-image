import json
import boto3
import os
from decimal import Decimal
import json
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client("s3")

def download_s3():
    # Replace with your own values
    download_path = os.getcwd()
    s3_location = get_s3_location()
    s3_path = s3_location.replace("s3://", "")
    bucket, key = s3_path.split("/", 1)
    print("Bucket:", bucket)
    print("Key:", key)
    try:
        s3.download_file(bucket, key, download_path)
        print("File downloaded successfully!")
    except Exception as e:
        print(f"Error downloading file: {e}")


def get_s3_location():
    # Open a file in read mode
    file_path = "config.json"
    with open(file_path, "r") as file:
        contents = json.loads(file.read())
    print("----------")
    print(contents)
    print("--------")
    print(contents['registry-name'])
    table_name = "siri-model-registry"
    table = dynamodb.Table(table_name)

    response = table.get_item(
        Key={"registry-name": contents['registry-name']})

    for version in response['Item']['versions']:
        if version['version'] == Decimal(contents['version']):
            s3_location = version['s3_location']
    return str(s3_location)


def lambda_handler():
    # TODO implement
    _ = download_s3()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    lambda_handler()
