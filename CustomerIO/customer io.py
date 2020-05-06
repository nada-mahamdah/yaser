import time
import pymysql
from segment_manager_py import SegmentManager

# 23161 958201
# select * from anubis_manager.user where team_user_id = 44823 or email = "tristanlagrone@gmail.com" or harri_id = 2203052;
# update anubis_manager.user set email = "tristanlagrone@gmail.com", harri_id = 2203052 where team_user_id = 44823;
env = "HARRI"
user_ids = [4178413]
# 1144015
if env == "HARRI":
    conn = pymysql.connect(host='35.171.94.111',
                           db="harri3_live",
                           user='nada.mahamdah',
                           password='tPKxF?U4$H^NF^fN',
                           port=3307)

    a = conn.cursor()
    segment_manager = SegmentManager()
    for user_id in user_ids:
        query = 'SELECT id, first_name, last_name, email FROM user where id = ' + str(user_id) + ' '
        count_row = a.execute(query)
        if count_row == 0:
            print ("user with id: " + str(user_id) + " does not exist or is deleted")
            continue
        user = a.fetchall()
        user_data = {
            'id': str(user_id),
            'email': user[0][3]
        }
        print (user_data)
        SegmentManager().register(str(user_id), user_data)
        time.sleep(3)
elif env == "TEAM":
    conn = pymysql.connect(host="35.171.94.111",
                           db="team",
                           user="nada.mahamdah",
                           password="tPKxF?U4$H^NF^fN",
                           port=3309)
    a = conn.cursor()
    segment_manager = SegmentManager()
    for user_id in user_ids:
        query = 'SELECT id, first_name, last_name, email FROM user where id = ' + str(user_id) + ' '
        count_row = a.execute(query)
        if count_row == 0:
            print ("user with id: " + str(user_id) + " does not exist or is deleted")
            continue
        user = a.fetchall()
        user_data = {
            'id': "team_{}".format(str(user_id)),
            'first_name': user[0][1],
            'last_name': user[0][2],
            'email': user[0][3]
        }
        print (user_data)
        SegmentManager().register("team_{}".format(str(user_id)), user_data)
