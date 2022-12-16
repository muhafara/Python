import json
import requests

def lambda_handler(event, context):
    postcode_List = []
    
    #getting postcoes
    postcode = event['rawQueryString']
    long_lat_url = "https://api.postcodes.io/postcodes/{}/".format(postcode)
    page_one = requests.get(long_lat_url)
    data_one = json.loads(page_one.content)
    Longitude = data_one['result']['longitude']
    Latitude = data_one['result']['latitude']
    
    ###nearest post code###
    nearest_postcode_url = 'https://api.postcodes.io/postcodes?lon={}&lat={}'.format(Longitude, Latitude)
    page_two = requests.get(nearest_postcode_url)
    data_two = json.loads(page_two.content)
    
   ##ceating list of nearest postcodes
    for element in data_two['result']:
        postcode_List.append(element['postcode'])
        
    #converting list into JSON 
    jsonString = json.dumps(postcode_List)
    print(type(jsonString))
    

    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
        'body' : jsonString
    }
