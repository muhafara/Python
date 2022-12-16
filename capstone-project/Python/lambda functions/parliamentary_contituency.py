import json
import requests


def lambda_handler(event, context):
    #postcode
    postcode = event['rawQueryString']
    constituency_url = "https://api.postcodes.io/postcodes/{}/".format(postcode)
    page = requests.get(constituency_url)

    data = json.loads(page.content)
    constituency = data['result']['parliamentary_constituency']
    
    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
        'body' : constituency
    }
