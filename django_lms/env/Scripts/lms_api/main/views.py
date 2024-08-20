

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import TeacherSerializer
from . import models
# Create your views here.

class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[IsAuthenticated]
class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[IsAuthenticated]
    
@csrf_exempt        
def teacher_login(request):
    email1=request.POST.get('email')
    password1=request.POST.get('password')
    teacherData=models.Teacher.objects.get(email=email1,password=password1)
    if teacherData:
       return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})      
