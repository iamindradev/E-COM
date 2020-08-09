from django.urls import path
from .import views 

urlpatterns = [
    path('login/', views.login , name="login"), #for the login of users
    path('mail_to_user/', views.send_mail, name="send_mail"),
    # path('register/', views.login , name="register")# for the registration of user

]
