from django.contrib import admin
from django.urls import path
from todo.views import Viewtask, Tasks, TaskDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Viewtask.as_view(), name="Task"),
    path('tasks/', Tasks.as_view(), name="TaskDB"),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name="TaskDB"),

]
