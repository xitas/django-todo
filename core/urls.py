from django.contrib import admin
from django.urls import path
from todo.views import Viewtask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Viewtask.as_view(), name="Task")
]
