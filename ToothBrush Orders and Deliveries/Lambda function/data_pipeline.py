
import json
import psycopg2
import os

def lambda_handler(event, context):
    print("event collected is {}".format(event))
    for record in event['Records'] :
        s3_bucket = record['s3']['bucket']['name']
        print("Bucket name is {}".format(s3_bucket))
        s3_key = record['s3']['object']['key']
        print("Bucket key name is {}".format(s3_key))
        from_path = "s3://{}/{}".format(s3_bucket, s3_key)
        print("from path {}".format(from_path))
        Access_key = os.getenv('AWS_Access_key')
        print(f'Access key = {Access_key}')
        Access_Secrete = os.getenv('AWS_Access_Secrete')
        print(f'Access secrete = {Access_Secrete}')
        dbname = os.getenv('dbname')
        print(f'This is the data base name = {dbname}')
        host = os.getenv('host')
        print(f'This is the host name = {host}')
        user = os.getenv('user')
        print(f'This is the username = {user}')
        password = os.getenv('password')
        print(f'This is the password = {password}')
        tablename = os.getenv('tablename')
        print(f'This is the table name = {tablename}')
        
    connection = psycopg2.connect(dbname = dbname,
                              host = host,
                              port = '5439',
                              user = user,
                              password = password)
                                                                
    print('after connection....')
    curs = connection.cursor()
    print('after cursor....')
    querry = "COPY {} FROM '{}' CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}'CSV DATEFORMAT 'auto' ignoreheader as 1;".format(tablename,from_path,Access_key,Access_Secrete)
    print("query is {}".format(querry))
    print('after querry....')
    curs.execute(querry)
    connection.commit()
    #print(curs.fetchmany(3))
    print('after execute....')
    curs.close()
    print('after curs close....')
    connection.close()
    print('after connection close....')