from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

from rest_framework.views import APIView
from rest_framework.response import Response

class Resttest(APIView):

    def get(self,request):
        return Response({"msg":"Successful"})
