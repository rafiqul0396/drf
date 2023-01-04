import requests 


endpoint ="https://httpbin.org/anything"
endpoint1="https://httpbin.org/anything"
get_response=requests.get(endpoint1,json={"query":"Hello world"})# i am getting some response from this websites

#print as text file
print(get_response.json())