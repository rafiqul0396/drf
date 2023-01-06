from django.http import  JsonResponse
import json
from products.models import Products
from  django.forms.models import model_to_dict

def  api_home(request,*args, **kwargs):
    model_data=Products.objects.all().order_by("?").first()
    data={}
    if model_data:
        data=model_to_dict(model_data,fields=['id','title'])
 
    return JsonResponse(data)

# Create your views here.
