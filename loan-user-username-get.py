import boto3
import json
from boto3.dynamodb.conditions import Key

def query_loandetails(username, dynamodb=None):
    
    dynamodb = boto3.resource('dynamodb')
    print(dynamodb)
    table = dynamodb.Table('Loan')
    
    response = table.query(
        IndexName="username-index",
        KeyConditionExpression=Key('username').eq(username)
    )
    return response
    

 

def lambda_handler(event, context):
    print(event)
    user = query_loandetails(event['params']['path']['username'])
    print(user)
    # response = {
    #         # if Item not in result:
    #             "statusCode": 200,
    #             "body": user["Items"]
            
    # }
    return user["Items"]