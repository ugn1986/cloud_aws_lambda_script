import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    data = event['body-json']
    table = dynamodb.Table('Loan')
    result = table.update_item(
        Key={
            'id': event['params']['path']['id']
        },
        ExpressionAttributeNames={
          '#date': 'date',
        },
        UpdateExpression='set durationofloan=:durationofloand, #date=:dated, loanamount=:loanamountd, loantype=:loantyped, rateofinterest=:rateofinterestd',
        ExpressionAttributeValues={
            ':durationofloand':data['durationofloan'],
            ':loanamountd':data['loanamount'],
            ':loantyped':data['loantype'],
            ':rateofinterestd':data['rateofinterest'],
            ':dated':data['date'],
        },
        ReturnValues='UPDATED_NEW',
    )
    # return {
    #     'statusCode': 200,
    #     'body': result['Attributes']
    # }
    
    return result['Attributes']
