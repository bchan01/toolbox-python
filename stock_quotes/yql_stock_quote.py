import requests
import json

'''
YQL Console: https://developer.yahoo.com/yql/console/
env 'store://datatables.org/alltableswithkeys'; select * from yahoo.finance.quotes where symbol in ("YHOO","AAPL","GOOG","MSFT")

REST URL: 
https://query.yahooapis.com/v1/public/yql?q=env%20'store%3A%2F%2Fdatatables.org%2Falltableswithkeys'%3B%20select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)%20&format=json&diagnostics=true&callback=

'''
query = 'select * from yahoo.finance.quote where symbol in ("FB","AAPL","GOOG","AMZN")'
r=requests.get('https://query.yahooapis.com/v1/public/yql', params='q='+query+'&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=')


https://query.yahooapis.com/v1/public/yql?q=env%20'store%3A%2F%2Fdatatables.org%2Falltableswithkeys'%3B%20select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)%20&format=json&diagnostics=true&callback=
parsed_json = json.loads(r.content.decode('utf-8'))

print(json.dumps(parsed_json))

for q in parsed_json['query']['results']['quote']: 
  for k,v in q.items(): 
    print ("%s: %s" % (k,v))