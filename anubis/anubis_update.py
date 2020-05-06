import requests
import time
# 1957528 or team_user_id = 40970;
f = open('Anubis_Manager.txt', 'a')
Users = [4178413, 4203066]

prod_env = "http://anubis-api.harri.com"
dev_env = "http://anubis-api.harridev.com"
cookie = {"session": "b5ad4cb28980e835e8315d8"}
platform = "HARRI"  # TEAM
for userId in Users:
    url = str(prod_env) + '/api/v1/policies/reindex?users_ids=' + str(userId) + '&platform=' + str(platform)
    print url
    r = requests.get(url, cookies=cookie)
    print(str(userId) + " is " + str(r.text))
    f.write(str(userId) + " is " + str(r.text) + "\n")
    # time.sleep(1)




