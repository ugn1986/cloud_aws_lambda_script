import json
import boto3
import os

import uuid
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    #get all the loans
    table = dynamodb.Table('Account')
    # result=table.scan()
    # id=uuid.uuid1();
    # print("loan id:")
    # print(id)
    result = table.get_item(
        Key={
            'username': event['params']['path']['username']
        }
    )
    rest=[]
    rest.append(result['Item'])
    
    return rest

    #post Loan
    # data = json.loads(event['body'])
    # table = dynamodb.Table('Loan')
    # print(data)
    # item = {
    #     'id': str(uuid.uuid1()),
    #     'username': data['username'],
    #     'loantype': data['loantype'],
    #     'loanamount': data['loanamount'],
    #     'date': data['date'],
    #     'rateofinterest': data['rateofinterest'],
    #     'durationofloan': data['durationofloan']
    # }
    # table.put_item(Item=item)

    # # create a response
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(item)
    # }

    # return response