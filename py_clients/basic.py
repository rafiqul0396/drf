import requests 
import json


endpoint ="http://localhost:8000/api/"
endpoint1="http://localhost:8000/api/"   #"http://127.0.0.1:8000/"
get_response=requests.get(endpoint,params={"abc":123},json={"query":"how are you"})# i am getting some response from this websites
Url="http://localhost:8000/stucreate/"

data_student={
    'name':'rafik',
    'roll':123,
    'city':'Noida'
}

json_data=json.dumps(data_student)
r=requests.post(url=Url,data=json_data)
data_new=r.json()
print(data_new)

#print as text file
#print(get_response.text)
print(get_response.json())