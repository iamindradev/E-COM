from django.shortcuts import render
import json
from .models import ingridients, order, address
from django.http import JsonResponse

# Create your views here.


def items(request):
    if request.method == "GET":
        response = list(ingridients.objects.all().values(
            'id', 'name', 'category', 'price', 'rating', 'description', 'image'))

    return JsonResponse(response, safe=False)


def makeorder(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # print(data)
        order.objects.create(**data)
        response = "created"
    return JsonResponse(response, safe=False)


def confirmorder(request):
    if request.method == "POST":
        data = json.loads(request.body)
        payment = data['payment']
        # address.objets.create(**)
        # print(data)
        response = list(order.bojects.all())
    return JsonResponse(response, safe=False)


def product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        id = data['id']
        response = list(order.objects.filter(buyer_id=id).values(
            'product_id__name', 'product_id__image', 'product_id__price'))
        # print(response)
    return JsonResponse(response, safe=False)
