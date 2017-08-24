import requests
import json

query1 = 'select Name,Symbol,LastTradePriceOnly from yahoo.finance.quote where symbol in ("BARC.L","AAPL","0700.HK","V03.SI","T8FS.SI")'
query2 = 'select * from yahoo.finance.quote where symbol in ("BARC.L","AAPL","0700.HK","V03.SI","T8FS.SI")'
r=requests.get('https://query.yahooapis.com/v1/public/yql', params='q='+query1+'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=')

parsed_json = json.loads(r.content.decode('utf-8'))
for q in parsed_json['query']['results']['quote']: 
  for k,v in q.items(): 
    print ("%s: %s" % (k,v))
