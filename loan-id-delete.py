import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table = dynamodb.Table('Loan')
    table.delete_item(
        Key={
            'id': event['params']['path']['id']
        }
    )
    response={"output":"Loan has been deleted"}
    return response
