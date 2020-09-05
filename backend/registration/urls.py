from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.login, name="login"),  # for the login of users
    # path('mail_to_user/', views.send_mail, name="send_mail"),
    # for the registration of user
    path('point/', views.point, name="test"),
    path('register/', views.register, name="register"),
    path('confirm/' , views.phoneverify , name =" phone_verify")

]
