import requests
import csv
import json
import pymysql.cursors
f = open('move_brand_backup.txt', 'a')
f2 = open('move_brand_query.txt', 'a')
f3 = open('move_brand_sync.txt', 'a')
env = "CORE"

brand_ids= '812216'
parent_ids = " "

if env == "CORE":

 connection = pymysql.connect(host='35.171.94.111',
                        port=3307,
                        user='nada.mahamdah',
                        password='tPKxF?U4$H^NF^fN',
                        db='harri3_live',
                        cursorclass=pymysql.cursors.DictCursor);


 with connection.cursor() as cursor2:
    query = "select * from brand where id in (" + str(brand_ids) + ") and deleted = 0;"
    f2.write(query+"\n")
    cursor2.execute(query)
    myresult1 = cursor2.fetchall()
    if myresult1:
        query="update brand set group_id =" + str(brand_ids) +" where id =" + str(brand_ids) +";"
        f2.write(query + "\n")
    query = "select * from brand_user where brand_id in  (" + str(brand_ids) + ") and type ='IMPLICIT';"
    f2.write(query + "\n")
    cursor2.execute(query)
    myresult1 = cursor2.fetchall()
    if myresult1:
        row = cursor2.execute(query)
        f.write("<<<<<<<brand_user>>>>>>>>>>" + "\n")
        for row in cursor2:
            f.write("INSERT INTO harri3_live.brand_user (`brand_id`, `user_id`, `type`, `created`, `updated`)  VALUES (" + str(row['brand_id']) + "," + str(row['user_id']) + "," + str(row['type']) + "," + str( row['created']) + "," + str(row['updated']) + ");" + "\n")
        query = "delete from harri3_live.brand_user where brand_id IN  (" + str(brand_ids) + ") and type ='IMPLICIT';"
        f2.write(query + "\n")

    query = "select * from brand where group_id in (" + str(brand_ids) + ") and deleted = 0;"
    f2.write(query + "\n")
    cursor2.execute(query)
    myresult1 = cursor2.fetchall()
    a = myresult1
    y = []

    for x in myresult1:
        y.append(str(x['id']))
    f2.write(" ######child :  {" + (', '.join(y)) + "}" + "\n")
    Brand_group = str (brand_ids)+","+ ', '.join(y)

    query ="select * from brand_job_reference join job on brand_job_reference.job_id = job.id where brand_job_reference.brand_id in ("+str(Brand_group)+")and job.brand_id not in (" + str(brand_ids) + ") ;"
    f2.write(query + "\n")
    cursor2.execute(query)
    myresult1 = cursor2.fetchall()

