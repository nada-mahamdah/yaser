import json
import requests
import csv
import pymysql.cursors
connection = pymysql.connect(host='35.171.94.111',
                        port=3307,
                        user='nada.mahamdah',
                        password='tPKxF?U4$H^NF^fN',
                        db='harri3_live',
                        cursorclass=pymysql.cursors.DictCursor);


url = 'https://anubis-api.harri.com/api/v1/brands/4002238/users'

cookie = {"session": "7f9fa7b4b2993ab35e313379"}
with open('nada.csv' , 'r') as csvFile:
 reader = csv.reader(csvFile)

 for row in reader:
        print(row)

        first_name = row[0]
        last_name = row[1]
        email_value = row[2]

        brands = row[3]
        brands = brands.split(",")
        print str(brands)




        with connection.cursor() as cursor2:
                query = " select user.email from user where user.email like '%" + str(email_value) +"%'"
                print query
                cursor2.execute(query)
                myresult2 = cursor2.fetchall()
                if  myresult2:
                  print " the user already exists user name " + str(first_name) + " and email is " + str(email_value)
                else:

                    payload_brands=[]
                    for row2 in brands:

                        payload_brands.append({'id': row2})



                    payload = {'access_types':["ALL"],'brands': payload_brands,'email':email_value,'first_name':first_name,'last_name':last_name}
                    print(payload)
                    r = requests.post(url=url, json=payload, cookies=cookie)
                    print r.text




