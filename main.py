import linenotif
import requests
import os
import datetime

reps = [
    "table",
    "hogwarts",
    "icy-bot"
]

a = []

noti = linenotif.Notify()
noti.setKey(os.getenv('LINE_TOKEN'))
for url in reps:
    name = url
    url = "https://" + url + ".aiceaeng.repl.co"
    res = requests.get(url)
    if str(res) == '<Response [200]>':
        a.append(name + ' : OK')
    else:
        noti.send(name + ' down!')
        a.append(name + ' : DOWN')
print('### Status\n')
print('')
for i in a:
    print(i + "  ")
print('Latest Update : ' + str(datetime.datetime.now()))
