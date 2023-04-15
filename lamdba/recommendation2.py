import json
import boto3
def lambda_handler(event, context):
    personalizeRt = boto3.client('personalize-runtime')

    response = personalizeRt.get_recommendations(
    campaignArn = 'arn:aws:personalize:us-east-1:774582796406:campaign/cmpgn-2',
    numResults = 10
)
    str='Top Items are: '
    for item in response['itemList']:
        str+=item['itemId']
        str=str+' '
    return {
        'statusCode': 200,
        'body': json.dumps(str)
    }
