from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rest/',views.Resttest.as_view(), name='rest'),
    path('<str:room_name>/', views.room, name='room'),
]