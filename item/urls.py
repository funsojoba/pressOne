from django.contrib import admin
from django.urls import path
from .views import ItemAPI

urlpatterns = [
    path("", ItemAPI.as_view(), name="list-item"),
    path("<str:item_id>", ItemAPI.as_view(), name="get-item"),
]
