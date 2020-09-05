from django.urls import path
from .import views

urlpatterns = [
    path("", views.items, name="for fetching items"),
    path("makeorder/" , views.makeorder, name="for making order"),
    path("confirmorder/" ,views.confirmorder, name="for confirming order") ,
    path("product/", views.product, name="for showing prodct")
]