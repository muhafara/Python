import json
import requests

def lambda_handler(event, context):
    # TODO implement
    #post code to get longitude and latitude
    postcode = event['rawQueryString']
    long_lat_url = "https://api.postcodes.io/postcodes/{}/".format(postcode)
    page_one = requests.get(long_lat_url)
    data_one = json.loads(page_one.content)
    Longitude = data_one['result']['longitude']
    Latitude = data_one['result']['latitude']
    planning_List = []
    url = "https://www.planit.org.uk/api/applics/json?lat={}&lng={}&krad=5.0&recent=30&pg_sz=5&sort=-start_date&compress=on".format(Latitude,Longitude)
    page = requests.get(url)
    data = json.loads(page.content)
    #appending data to list
    for element in data['records']:
        planning_List.append(element['address'])
        planning_List.append(element['area_name'])
        planning_List.append(element['description'])
        planning_List.append(element['scraper_name'])
        planning_List.append(element['other_fields']['ward_name'])
        planning_List.append("new_line")
        jsonString = json.dumps(planning_List)
    return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
        'body' : jsonString
    }