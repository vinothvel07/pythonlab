import json

import csv


def flattenjson( b, delim ):
    val = {}
    for i in b.keys():
        if isinstance( b[i], dict ):
            get = flattenjson( b[i], delim )
            for j in get.keys():
                val[ i + delim + j ] = get[j]
        else:
            val[i] = b[i]

    return val


input = open('data.json')



employee_parsed = json.load(input)

input = map( lambda x: flattenjson( x, "__" ), employee_parsed )

print(input)


emp_data = employee_parsed['items']

# open a file for writing

employ_data = open('EmployData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0

for emp in emp_data:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()