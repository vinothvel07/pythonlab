import json
import csv

startdate = '2019-02-20'
with open('test1.json') as f:
      js_data =  json.loads(f.read())

js_span = js_data['members']

count=0

for js in js_span:
    if(count==0):
        header=list(js.keys()) + ['startdate']


print(header)



with open('output.csv' ,'w') as op:
    w = csv.DictWriter(op, header)
    w.writeheader()
    for js in js_span:
        w.writerows(js + startdate)