import json
import boto3


dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('Loan')
    result = table.get_item(
        Key={
            'id': event['params']['path']['id']
        }
    )
    # response = {
    #     "statusCode": 200,
    #     "body": result['Item']
    # }
    return result['Item']
