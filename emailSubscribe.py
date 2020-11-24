import os
import json
import boto3
from datetime import datetime
from botocore.exceptions import ClientError

region = os.environ['AWS_REGION']
client = boto3.client('dynamodb')
resDb = boto3.resource('dynamodb')


def _send_email(email_to_subscribe, email_link):
    """Function to send email
    If email is not present in database
    Send confirmation link that hits the confirm_and_redirect API

    Args:
        email_to_subscribe ([string]): [user email entered in database]
        email_link ([string]): [link for confirmation]
    """
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    # SENDER = "Sender Name <seudogame@gmail.com>"
    SENDER = "seudogame@gmail.com"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = "shrestha.uts@gmail.com"

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    #CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = region

    # The subject line for the email.
    SUBJECT = "Amazon SES Test (SDK for Python)"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                 )

    # The HTML body of the email.
    BODY_HTML = f"""<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
          AWS SDK for Python (Boto)</a>.</p>
        <a href= {email_link}> Confirm </a>
    </body>
    </html>
                """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


def lambda_handler(event, context):
    """Define expected JSON format, REST method, etc.
    Collect email from user and check if it is present in database
    If not present send confirmation link to email

    Args:
        event ([dictionary]): [ ]
        context ([__main__.LambdaContext]): [ ]

    Returns:
        [dictionary]: [returns return_payload with status code and related message]
    """
    email_link_is = os.environ['EMAIL_LINK_IS']
    # Retrieve input email
    email_to_subscribe = event['email']
    # Retrieve present email data
    response = client.scan(TableName='EmailSubscribe')
    response = response['Items']
    # Set token to false
    s = False

    for line in response:
        item = line['email']
        # Check to see if the email_to_subscribe is already present in the database
        # IF present, return 200 OK with meessage : You are already subscribed
        if email_to_subscribe in item['S']:
            # If present set token to true
            s = True
            return_payload = {
                'statusCode': 200,
                'body': json.dumps('You are already our member!')

            }
    # IF not present, return 200 OK with message, Please check your email for confirmation link.
    # Insert email into the database
    if s == False:
        table = resDb.Table('EmailSubscribe')
        input = {
            'email': email_to_subscribe,
            'verified': 'false'
        }
        table.put_item(Item=input)
        email_link = f'{email_link_is}?email={email_to_subscribe}'
        # Invoke Amazon SESs
        _send_email(email_to_subscribe, email_link)
        return_payload = {
            'statusCode': 200,
            'body': json.dumps('Please check your email for confirmation link.')
        }

    # Handle for CORS
    return_payload.update({
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
        }
    })

    return return_payload
