from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render
from backend.settings import EMAIL_HOST_USER
from .models import user_data
from django.template import loader, Context
import json
from django.http import JsonResponse
from django.shortcuts import render


# login
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        passwd = data['password']
        if user_data.objects.filter(email=email, password=passwd):
            email_db = user_data.objects.get(email=email)
            if email == email_db:
                passwd_db = user_data.objects.get(email=email)
                if passwd == passwd_db:
                    response = "logged in successfully"
                else:
                    response = "wrong password"
            else:
                response = "wrong mail"
        else:
            response = "you haven't registered yet"
    return JsonResponse(response, safe=False)

# register


def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        email = data['email']
        # if user_data.objects.filter(email=email).exists():
        #     response = "user exists"
        # else:
            # user_data.objects.create(**data)
        response = "user created"
        subject = "email confirmation"
        variables = {
            'email': email,
            'fname': data['fname'],
            'lname': data['lname']

        }
        print(variables)
        with open(settings.BASE_DIR + "/registration/template/message.txt") as f:
            text_content =  f.read()
            html_content = loader.get_template('message.html').render(variables)        
            msg = EmailMultiAlternatives(subject, text_content, EMAIL_HOST_USER, [email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        return JsonResponse(response, safe=False)


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
