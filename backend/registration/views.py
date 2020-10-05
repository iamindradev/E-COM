from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render
from backend.settings import EMAIL_HOST_USER
from .models import user_data
from django.template import loader, Context
import requests
import json
import random
import math
from django.http import JsonResponse
from django.shortcuts import render

# logic to generate otp


def onetimepass():
    data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    leng = len(data)
    otp = ""
    for i in range(0, 6):
        otp += data[math.floor(random.random()*leng)]
    print("your otp is", otp)
    return otp

# def phoneverify(request):
#     if request.method =="POST":

#     return JsonResponse(response.text, safe = False)


# login
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        username = data['username']
        passwd = data['password']
        if user_data.objects.filter(identity=username):
            passwd_lst = list(user_data.objects.filter(
                identity=username).values('password', 'id'))
            print(passwd_lst)
            passwd_data = passwd_lst[0]
            # id_data= passwd_lst[1]
            id=passwd_data['id']
            passwd_db = passwd_data['password']
            print(passwd_db,id)
            if passwd == passwd_db:
                if request.session.test_cookie_worked():
                    response=id

                else:
                    # request.session.set_test_cookie()
                    # request.session['id'] = id
                    response = id
            else:
                response = "wrong password"
        else:
            response = "you haven't registered yet or wrong mail/contact"
    return JsonResponse(response, safe=False)


def point(request):
    if request.method == "GET":
        username = "devendra"
        if request.session.test_cookie_worked():
            response = "logged in successfully"

        else:
            request.session.set_test_cookie()
            request.session['username'] = username
            response = "logged in successfully"
    return JsonResponse(response, safe=False)

# register


def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        identity = data['identity']
        typ = data['typ']
        if user_data.objects.filter(identity=identity).exists() == True:
            # or user_data.objects.filter(email= identity ).exists()
            response = "user exists"
        else:
            if typ == "phone":
                data = json.loads(request.body)
                contact = data['identity']
                url = "https://www.fast2sms.com/dev/bulk"
                otp = onetimepass()

                payload = "sender_id=FSTSMS&message=THIS%20IS%20YOUR%20OTP%20FOR%20CONFIRMATION%20OF%20CONTACT%20NUMBER%20ON%20DEVENDRA'S%20E-CART%20 :" + \
                    otp+"&language=english&route=p&numbers="+contact
                headers = {
                    'authorization': "VdTeLyCubRJonDXW9wt2m7ENIB5KgcZxUkhOMpiYQ43AHz0fFSk1brgcdECAmMXu4OVQFz95LGUBPxSJ",
                    'Content-Type': "application/x-www-form-urlencoded",
                    'Cache-Control': "no-cache",
                }
                resp = requests.request(
                    "POST", url, data=payload, headers=headers)
                # fname=data['fname']
                # lname=data['lname']
                # password=data['password']
                print(resp.text)
                user_data.objects.create(otp=otp, **data)
                response = "msg sent and user created"

            else:
                email = data['identity']
                # response = "user created with mail"
                response = list(user_data.objects.all())
                print(response)
                subject = "email confirmation"
                variables = {
                    # 'otp':onetimepass(),
                    'email': email,
                    'fname': data['fname'],
                    'lname': data['lname'],
                    'password': data['password'],
                    'typ': data['typ']

                }
                print(variables)
                with open(settings.BASE_DIR + "/registration/template/message.txt") as f:
                    text_content = f.read()
                    html_content = loader.get_template(
                        'message.html').render(variables)
                    msg = EmailMultiAlternatives(
                        subject, text_content, EMAIL_HOST_USER, [email])
                    msg.attach_alternative(html_content, "text/html")
                    msg.send()
                    # user_data.objects.create(email=email,)
                    user_data.objects.create(**data)

    return JsonResponse(response, safe=False)


def phoneverify(request):
    if request.mehtod == "POST":
        data = json.loads(request.body)
        otp = data['otp']
        if user_data.objects.filter(otp=otp).exists() == True:
            response = "verified"
        else:
            response = "wrong otp"
    return JsonResponse(response, safe=False)
#added some comment that some work is left