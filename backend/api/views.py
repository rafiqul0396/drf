from django.http import  JsonResponse
import json

def  api_home(request,*args, **kwargs):

    body=request.body # byte string of Json Data
    print(request.GET)
    print(request.POST)
    
    data={}
    try:
        data=json.loads(body)
    except :
        pass

    print(data.keys())
    return JsonResponse({"message":"hi, there any on take my response"})

# Create your views here.
