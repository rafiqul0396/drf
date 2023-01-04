from django.http import  JsonResponse
import json
from products.models import Products

def  api_home(request,*args, **kwargs):
    model_data=Products.objects.all().order_by("?").first()
    data={}
    if model_data:
        data['id']=model_data.id
        data['titile']=model_data.title
        data['contents']=model_data.contents
        data['price']=model_data.price
 
    return JsonResponse(data)

# Create your views here.
