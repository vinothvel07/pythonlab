import json
import os
input = open('data.json')


print(os.getenv('proxy_http'))
data = json.load(input)

#print(data['items'])


#for row in data['items']:
    #print(row.keys())
    #print(row['user'].values())