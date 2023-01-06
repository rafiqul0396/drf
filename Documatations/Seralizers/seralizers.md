## Python JSON

- JSON is a syntax for storing and exchanging data.

- JSON is text, written with **JavaScript object notation**

```python
import json
```

#### Parse JSON - Convert from JSON to Python

If you have a JSON string, you can parse it by using the json.loads() method.

- the result will be python dictionary

```python
  import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
```

#### Convert from Python to JSON

If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

```python
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
```

> You can convert Python objects of the following types, into JSON strings:

 1. dict
 2. list
 3. tuple
 4. string
 5. int
 6. float
 7. True
 8. False
 9. None

```python
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
```

###### Python | JSON
```table
dict |Object
list |Array
tuple |Array
str |String
int |Number
float |Number
True |true
False |false
None |null
```
```python
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
```


### Serializers
Serializers in Django REST Framework are responsible for converting objects into data types understandable by javascript and front-end frameworks. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data. The serializers in REST framework work very similarly to Django’s Form and ModelForm classes. The two major serializers that are most popularly used are ModelSerializer and HyperLinkedModelSerialzer.


- Creating and Using Serializers
- ModelSerializer
- HyperLinkedModelSerializer
- Serializer Fields
- Core arguments in serializer fields



##### Creating and Using Serializers


To create a basic serializer one needs to import serializers class from rest_framework and define fields for a serializer just like creating a form or model in Django. 
```python
# import serializer from rest_framework
from rest_framework import serializers

# create a serializer
class CommentSerializer(serializers.Serializer):
	# initialize fields
	email = serializers.EmailField()
	content = serializers.CharField(max_length = 200)
	created = serializers.DateTimeField()
```
