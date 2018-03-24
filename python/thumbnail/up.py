import urllib.request
import json
import datetime
import subprocess

#datetimeから現在日時を取得
now = datetime.datetime.now() # => datetime.datetime(2017, 7, 1, 23, 15, 34, 309309)
today = datetime.date.today()
print(now)
print(today)


#webapiからjsonの取得
a = 'http://api.nhk.or.jp/v2/pg/list/130/g1/'
b = 'key'
print(a + str(today) + b)
url = a + str(today) + b

response = urllib.request.urlopen(url)
content = json.loads(response.read().decode('utf8'))


#イベントIDとスタートタイムのみを抽出
for item in content['list']['g1']:
        print(item['event_id'], ':', item['start_time'])


#コマンドの実行
res = subprocess.run(['cp', '/Library/WebServer/Documents/thumbnail/0000/test.png', '/Library/WebServer/Documents/thumbnail/1111/'])
print (res)
