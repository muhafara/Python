import pymysql

'''Database Connection'''
connection = pymysql.connect(host='global-database-childern-data.cqsnotpqnv64.us-east-1.rds.amazonaws.com',
                             user='admin', password='*****')
cursor = connection.cursor()
cursor.connection.commit()

#SELECT * FROM TABLE
def countriestable():
    sql = '''SELECT * FROM GLOBAL_DATABASE_CHILDER_EDUCATION.COUNTRIES;'''
    cursor.execute(sql)
    for row in cursor:
        print("COUNTRY_ID = ", row[0])
        print("Country_NAME = ", row[1], "\n")

#SELECT * FROM TABLE
def unicefidtable():
    sql = '''SELECT * FROM GLOBAL_DATABASE_CHILDER_EDUCATION.UNICEF_ID;'''
    cursor.execute(sql)
    for row in cursor:
        print("UNICEF_ID", row[0])
        print("ISO_CODE", row[1])
        print("CHILDERN_WITH_FUNCTIONAL_DISABILITIES", row[2])
        print("CHILDERN_WITHOUT_FUNCTIONAL_DISABILITIES",  row[3])
        print("COUNTRY_ID", row[4])
        print("DEVELOPMENT_ID", row[5])
        print("CATAGORY_ID", row[6])
        print("SOURCE_ID", row[7])
        print("REGION_ID", row[8], "\n")

#--> ORDERBY
def byOrderfunction():
    sql = '''SELECT * FROM GLOBAL_DATABASE_CHILDER_EDUCATION.COUNTRIES ORDER BY COUNTRY_NAME DESC'''
    cursor.execute(sql)
    for row in cursor:
        print("COUNTRY_ID = ", row[0])
        print("Country_NAME = ", row[1], "\n")

#--> WHERECLAUSE
def whereclause():
    sql = '''SELECT * FROM GLOBAL_DATABASE_CHILDER_EDUCATION.COUNTRIES WHERE COUNTRY_NAME LIKE 'G%' '''
    cursor.execute(sql)
    for row in cursor:
        print("COUNTRY_ID = ", row[0])
        print("Country_NAME = ", row[1], "\n")

#CALCULATING AVERAGE NYMBER OF UNICEF_POINT AVG
def usingavgfunc():
    sql = '''SELECT COUNT(CHILDERN_WITHOUT_FUNCTIONAL_DISABILITIES)FROM GLOBAL_DATABASE_CHILDER_EDUCATION.UNICEF_ID'''
    cursor.execute(sql)
    print("Average is : ",cursor.fetchall())

#Using Join with UNICEF_TABLE
def usingjoin():
    sql = '''SELECT  UID.ISO_CODE, UID.CHILDERN_WITH_FUNCTIONAL_DISABILITIES, 
    UID.CHILDERN_WITHOUT_FUNCTIONAL_DISABILITIES, 
    COU.COUNTRY_NAME, DS.DEVELOPMENT_STATUS, 
    CAT.CATAGORY_NAME, 
    DDS.DATA_SOURCE_NAME, 
    REG.REGION_NAME 
    FROM GLOBAL_DATABASE_CHILDER_EDUCATION.UNICEF_ID UID
    JOIN COUNTRIES COU ON COU.COUNTRY_ID = UID.COUNTRY_ID 
    JOIN DEVELOPMENT_STATUS DS ON DS.DEVELOPMENT_ID = UID.DEVELOPMENT_ID 
    JOIN CATAGORY CAT ON CAT.CATAGORY_ID = UID.CATAGORY_ID 
    JOIN DATA_SOURCE DDS ON DDS.SOURCE_ID = UID.SOURCE_ID 
    JOIN REGION REG ON REG.REGION_ID = UID.REGION_ID'''

    cursor.execute(sql)
    for row in cursor:
        print("UNICEF_ID", row[0])
        print("ISO_CODE", row[1])
        print("CHILDERN_WITH_FUNCTIONAL_DISABILITIES", row[2])
        print("CHILDERN_WITHOUT_FUNCTIONAL_DISABILITIES",  row[3])
        print("COUNTRY_NAME", row[4])
        print("DEVELOPMENT_STATUS", row[5])
        print("CATAGORY_NAME", row[6])
        print("DATA_SOURCE_NAME", row[7])
        print("REGION_NAME", row[8], "\n")



usingjoin()
#usingavgfunc()
#whereclause()
#byOrderfunction()
#unicefidtable()
#countriestable()