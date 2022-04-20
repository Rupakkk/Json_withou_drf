from django.http import JsonResponse
from django.shortcuts import render
from .models import Student
from django.views import View

# Create your views here.
class StudentView(View):
    def get(self,request):
        student = list(Student.objects.all().values())
        return JsonResponse(student,safe=False)