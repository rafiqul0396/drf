from django.http import  JsonResponse


def  api_home(request,*args, **kwargs):
    return JsonResponse({"message":"hi, there any on take my response"})
# Create your views here.
