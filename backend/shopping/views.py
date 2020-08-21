from django.shortcuts import render
import json
from .models import ingridients , order
from django.http import JsonResponse

# Create your views here.
def items(request):
    if request.method=="GET":
        response = list(ingridients.objects.all().values('name','category','price','rating','description','image'))
    
    return JsonResponse(response, safe=False)
