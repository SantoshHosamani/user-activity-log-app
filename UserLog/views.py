from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponseNotFound
from .models import User, ActivityPeriods

# Create your views here.
class get_user_activity_log(APIView):

    def get(self,request):
        user_activity_info = User.objects.all()
        return JsonResponse(user_activity_info)
