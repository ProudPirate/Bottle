import json
import boto3

resDb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    """[verify the user email and redirect the user to www.google.com]

    Args:
        event ([dictionary]): [ ]
        context ([__main__.LambdaContext]): [ ]

    Returns:
        [dictionary]: [returns response with appropriate status code]
    """
    # get email from input
    email_to_confirm = event['queryStringParameters']
    email_to_confirm = email_to_confirm['email']
    # query input and update verified attribute to true
    table = resDb.Table('EmailSubscribe')
    input = {
        'email': email_to_confirm,
        'verified': 'true'
    }
    table.put_item(Item=input)
    # return 302 redirect response
    response = {}
    response["statusCode"] = 302
    response["headers"] = {'Location': 'https://www.google.com'}
    data = {}
    response["body"] = json.dumps(data)
    return response
