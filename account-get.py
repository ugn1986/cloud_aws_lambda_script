import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Account')

def lambda_handler(event, context):
    response = table.scan()
    for item in response['Items']:
        print(item)
    
    return {
        'statusCode': 200,
        'body': response['Items']
    }
