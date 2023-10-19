from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


class Viewtask(APIView):

    data = {
        "Task1": {
            'title': "Task 1",
            'description': "This is a task 1",
            'status': "pending"
         },
        "Task2":{
            'title': "Task 2",
            'description': "This is a task 2",
            'status': "pending"
        }
    }

    def get(self, request):
        return Response(self.data)

    def post(self, request):
        task_data = request.data
        self.data["Task3"] = task_data
        return Response(self.data)

    def put(self, request):
        task_data = request.data
        task_data['status'] = 'complete'
        return Response(task_data)

