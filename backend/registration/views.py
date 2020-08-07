from django.shortcuts import render
from .models import user_data
import json 
from django.http import JsonResponse

#login
def login(request):
    if request.method == "POST":
        data= json.loads(request.body)
        email= data['email']
        passwd= data['password']
        if user_data.objects.filter(email=email, password= passwd):
            email_db= user_data.objects.get(email=email)
            if email==email_db:
                passwd_db=user_data.objects.get(email=email)
                if passwd==passwd_db:
                    response="logged in successfully"
                else:
                    response="wrong password"
            else:
                response="wrong mail"
        else:
            response="you haven't registered yet"
    return JsonResponse(response ,safe= False)

#register
# def register()