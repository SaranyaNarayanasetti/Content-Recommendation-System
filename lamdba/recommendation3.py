import json
import boto3
def lambda_handler(event, context):
    personalizeRt = boto3.client('personalize-runtime')

    response = personalizeRt.get_recommendations(
    campaignArn = 'arn:aws:personalize:us-east-1:774582796406:campaign/cmpgn-1',
    userId=event["uid"],
    itemId=event["items"]
)
    str='Personalized Rankings  are:\n'
    for item in response['personalizedRanking']:
        str+=item['itemId']+item["score"]
        str=str+'\n'
    return {
        'statusCode': 200,
        'body': json.dumps(str)
    }
