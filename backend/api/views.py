#from django.http import  JsonResponse
import json
from products.models import Products
from  django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students
from .serailizer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt

@api_view(["POST"])
def  api_home(request,*args, **kwargs):
    model_data=Products.objects.all().order_by("?").first()
    data={}
    if model_data:
        data=model_to_dict(model_data,fields=['id','title'])
 
    return Response(data)


def  student_deatails(request):
    stu=Students.objects.all().order_by("?").first()
    print(stu)
    serailzed=StudentSerializer(stu)
    print(serailzed)
    print(serailzed.data)
    json_data=JSONRenderer().render(serailzed.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def Student_create(request):

    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        sera_data=StudentSerializer(data=pythondata)

        if(sera_data.is_valid()):
            sera_data.save()

            res={'msg':'Student created'}
            json_dat=JSONRenderer().render(res)
            return HttpResponse(json_dat,content_type='application/json')
        json_ret=JSONRenderer().render(sera_data.errors)
        return HttpResponse(json_ret,content_type='application/json')
        







# Create your views here.
