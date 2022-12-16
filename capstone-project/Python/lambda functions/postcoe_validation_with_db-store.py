import json
import requests
import pymysql
import datetime


def lambda_handler(event, context):
    # TODO implement
    postcode = event['rawQueryString']
    current_time = datetime.datetime.now()
    url = 'https://api.postcodes.io/postcodes/{}/validate'.format(postcode)
    page = requests.get(url)
    data = json.loads(page.content)
    validator = data['result']
    #checks if postcode exists
    if validator:
        #'''Database Connection'''
       connection = pymysql.connect(host='lin-11314-6893-mysql-primary.servers.linodedb.net', user='user_10', password='Ttqd6gA_WEg5~97-3Cw4q4gAW-sELrdsy_QAh',db='db10',ssl={"fake_flag_to_enable_tls":True})
       cur = connection.cursor()
       cur.execute("""INSERT INTO db10.api_time_records
                    (post_code, time)
                     VALUES(%s,%s)""", (postcode, current_time))
       cur.connection.commit()
       print("successfully inserted into database")
       print("connection succesfull")
    else:
        print("connection not succesfull")
    return {
    'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5500',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    },
    'body': validator
    }
