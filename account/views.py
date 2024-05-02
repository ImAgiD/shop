import datetime

from django.shortcuts import render
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer

User = get_user_model()

class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_axception=True):
            serializer.save()
        return Response('Вы успешно зарегистрировались', 201)
        
class ActivationView(APIView):
    def get(self, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code)
        if not user:
            return Response('Пользователь не найден!', 404)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активировано', 200)