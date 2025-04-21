from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, taskList
from . import views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('tasks/', views.taskList, name="tasks"),
    path('', taskList)
]

