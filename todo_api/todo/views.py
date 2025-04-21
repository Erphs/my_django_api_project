from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


def taskList(request):
    return JsonResponse({"message": "its work"})


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

