import requests
import json

query1 = 'select * from yahoo.finance.historicaldata where symbol = "GOOG" and startDate = "2010-01-01" and endDate = "2017-08-01"'
r=requests.get('https://query.yahooapis.com/v1/public/yql', params='q='+query1+'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=')

parsed_json = json.loads(r.content.decode('utf-8'))

print(json.dumps(parsed_json))

'''
for q in parsed_json['query']['results']['quote']: 
  for k,v in q.items(): 
    print ("%s: %s" % (k,v))
'''