import requests 


endpoint ="https://httpbin.org/anything"
endpoint1="http://localhost:8000/"   #"http://127.0.0.1:8000/"
get_response=requests.get(endpoint1)# i am getting some response from this websites

#print as text file
print(get_response.text)