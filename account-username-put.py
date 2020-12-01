import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    data = event['body-json']
    table = dynamodb.Table('Account')
    result = table.update_item(
        Key={
            'username': event['params']['path']['username']
        },
        ExpressionAttributeNames={
          '#name': 'name',
          '#state': 'state',
        },
        UpdateExpression='set accounttype=:accounttyped, address=:addressd, contact=:contactd, country=:countryd, DOB=:DOBd, email=:emaild, #name=:named, pan=:pand, password=:passwordd, #state=:stated',
        ExpressionAttributeValues={
            ':accounttyped':data['accounttype'],
            ':addressd':data['address'],
            ':contactd':data['contact'],
            ':countryd':data['country'],
            ':DOBd':data['DOB'],
            ':emaild':data['email'],
            ':named':data['name'],
            ':pand':data['pan'],
            ':passwordd':data['password'],
            ':stated':data['state'],
            
        },
        ReturnValues='UPDATED_NEW',
    )
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    return result['Attributes']
