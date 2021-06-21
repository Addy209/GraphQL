from django.contrib import admin
from django.urls import path, include
from .views import GetTestData
urlpatterns = [
    path('',GetTestData.as_view())
]