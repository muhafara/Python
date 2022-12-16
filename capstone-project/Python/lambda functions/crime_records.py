import json
import requests
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    postcode = event['rawQueryString']
    long_lat_url = "https://api.postcodes.io/postcodes/{}/".format(postcode)
    page_one = requests.get(long_lat_url)
    data_one = json.loads(page_one.content)
    Longitude = data_one['result']['longitude']
    Latitude = data_one['result']['latitude']
    counter = 0
    crime_List = []
    current_year = datetime.now().year
    current_month = datetime.now().month
    url = "https://data.police.uk/api/crimes-street/all-crime?lat={}&lng={}&date{}-{}".format(Latitude,Longitude,current_year,current_month)
    page = requests.get(url)
    data = json.loads(page.content)
    for element in data:
        counter = counter + 1
    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
        'body': counter
    }
