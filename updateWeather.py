import psycopg2 as pg
import requests
import boto3

def updateWeather(event,context):
    print("hi")
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=CWB-1C90EC71-FB67-47EB-B2D7-AA7829DBB55B&format=JSON&stationId=466940&elementName=TIME,TEMP,D_TX,D_TN,D_TS,Weather&parameterName=CITY'
    data = requests.get(url, timeout=10)
    data_json = data.json()
    weather = data_json['records']['location'][0]['weatherElement']
    weather_value = {'timestamp': data_json['records']['location'][0]['time']['obsTime']}
    for i in range(len(weather)):
        weather_value.update({weather[i]['elementName']: weather[i]['elementValue']})
    weather = weather_value
    conn = pg.connect(
        host="database-2.cf5cyqhkjo5q.us-east-1.rds.amazonaws.com",
        port=5432,
        user="postgres",
        password="sam42671209",
        database="postgres"
    )
    cursor = conn.cursor()
    sql = f"insert into weather(timestamp,temp,weather,d_tx,d_tn,d_ts) " \
          f"values('{weather['timestamp']}',{weather['TEMP']}, '{weather['Weather']}',{weather['D_TX']},{weather['D_TN']},{weather['D_TS']})"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()