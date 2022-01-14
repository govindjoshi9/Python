
import json

data = '{"var1":"Harry","var2":56}'
#print(data)

parsad = json.loads(data)
print(type(parsad))