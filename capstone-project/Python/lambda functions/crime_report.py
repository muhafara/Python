import json
import requests
from datetime import datetime

def lambda_handler(event, context):
    postcode = event['rawQueryString']
    long_lat_url = "https://api.postcodes.io/postcodes/{}/".format(postcode)
    page_one = requests.get(long_lat_url)
    data_one = json.loads(page_one.content)
    Longitude = data_one['result']['longitude']
    Latitude = data_one['result']['latitude']
    current_year = datetime.now().year
    current_month = datetime.now().month
    url = "https://data.police.uk/api/crimes-street/all-crime?lat={}&lng={}&date{}-{}".format(Latitude,Longitude,current_year,current_month)
    page = requests.get(url)
    data = json.loads(page.content)
    counter = 0
    crime_List = []
    for element in data:
        #counter will append 10 records only
        counter = counter + 1
        if(counter<=10):
                crime_List.append(element['category'])
                crime_List.append(element['location']['street']['id'])
                crime_List.append(element['location']['street']['name'])
                crime_List.append(element['month'])
    #print("crime records are : ",crime_List,"\n")
    jsonString = json.dumps(crime_List)
    
    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
        'body' : jsonString
    }


