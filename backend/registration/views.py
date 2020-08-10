from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render
from backend.settings import EMAIL_HOST_USER
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
def register(request):
    if request.method=="POST":
        data= json.loads(request.body)
        print(data)
        email_user= data['email']
        subject="test mail"
        message="template"
        send_mail(
            subject, message, EMAIL_HOST_USER, [email_user],
            fail_silently=False,
        )
    JsonResponse("mail sent" , safe =False)



# def send_mail(request):
#     if request.method=="POST":
#         subject="for confirmation"
#         message="hello"
#         from_email="yadavdevendra@99876@gmail"
#         data= json.loads(request.body)
#         email_user= data['email']
#         print(email_user)
#         if subject and message and from_email:
#             try:
#                 send_mail(subject, message, from_email, data['email'])
#             except BadHeaderError:
#                     return HttpResponse('Invalid header found.')
#             return HttpResponseRedirect('/contact/thanks/')
#         else:
#             # In reality we'd use a form class
#             # to get proper validation errors.
#             return JsonResponse( 'Make sure all fields are entered and valid.')
# # def register()