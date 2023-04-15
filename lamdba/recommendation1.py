import json
import boto3
def lambda_handler(event, context):
    personalizeRt = boto3.client('personalize-runtime')

    response = personalizeRt.get_recommendations(
    campaignArn = 'arn:aws:personalize:us-east-1:774582796406:campaign/campgn-3',
    userId = event['id'],
    numResults = 10
)
    str='User Items are: '
    for item in response['itemList']:
        str+=item['itemId']+" "
    return {
        'statusCode': 200,
        'body': json.dumps(str)
    }
