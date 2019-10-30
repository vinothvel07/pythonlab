import json
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print (x.name, x.hometown.name, x.hometown.id)

