import requests 



endpoint ="https://httpbin.org/anything"
endpoint1="http://localhost:8000/api/"   #"http://127.0.0.1:8000/"
get_response=requests.get(endpoint1,params={"abc":123},json={"query":"how are you"})# i am getting some response from this websites

#print as text file
#print(get_response.text)
print(get_response.json())