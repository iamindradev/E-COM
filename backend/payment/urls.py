from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.initiate_payment, name="for initiation of payment"),
    path('callback/', views.callback, name="for call back"),
    path('paydata/',views.paydata, name="for getting data")
]
