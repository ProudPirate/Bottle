import json
import boto3

resDb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    """[summary]

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    # TODO implement
    email_to_confirm = event['queryStringParameters']
    email_to_confirm = email_to_confirm['email']
    print(email_to_confirm)
    table = resDb.Table('EmailSubscribe')
    input = {
        'email': email_to_confirm,
        'verified': 'true'
    }
    table.put_item(Item=input)
    response = {}
    response["statusCode"] = 302
    response["headers"] = {'Location': 'https://www.google.com'}
    data = {}
    response["body"] = json.dumps(data)
    return response
