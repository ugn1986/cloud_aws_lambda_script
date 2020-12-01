import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Account')

def lambda_handler(event, context):
    
    result = table.get_item(
        Key={
            'username': event['username']
        }
    )
    if 'Item' not in result:
        response=table.put_item(Item=event)
    else:
        response={"output":"user already exists"}
    
    # result=table.put_item(Item=event)
    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('User added successfully')
    # }
    # rest=[]
    # rest.append(response)
    # return rest
    return response
