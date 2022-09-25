import json, boto3

client = boto3.client('dynamodb')
TableName = 'counter-db1'

def lambda_handler(event, context):
    
    '''
    data = client.get_item(
        TableName='counter-db1',
        Key = {
            'id': {'S': 'view-count'}
        }
    )
    '''
    
    #data['Item']['Quantity']['N'] = str(int(data['Item']['Quantity']['N']) + 1)
    
    response = client.update_item(
        TableName='counter-db1',
        Key = {
            'id': {'S': 'view-count'}
        },
        UpdateExpression = 'ADD Quantity :inc',
        ExpressionAttributeValues = {":inc" : {"N": "5"}},
        ReturnValues = 'UPDATED_NEW'
        )
        
    value = response['Attributes']['Quantity']['N']
    
    return {      
            'statusCode': 200,
            'body': value}
