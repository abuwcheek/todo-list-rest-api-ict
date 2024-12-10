from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Tasks
from .serializers import TaskSerializer, TaskUpdateSerializer


# APIView

class TaskView(APIView):
     def get(self, request):
          task = Tasks.objects.all()
          serializer = TaskSerializer(task, many=True)
          return Response(serializer.data)


     def post(self, request):
          serializer = TaskSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskRetriveAPIView(APIView):
     def get(self, request, pk):
          task = Tasks.objects.get(id=pk)
          serializer = TaskSerializer(task)
          return Response(serializer.data)


     def put(self, request, pk):
          task = Tasks.objects.get(id=pk)
          serializer = TaskUpdateSerializer(instance=task, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     
     def delete(self, request, pk):
          task = Tasks.objects.get(id=pk)
          task.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)


# generics

class TaskListAPIVieW(ListAPIView):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer

class TaskCreateAPIVieW(CreateAPIView):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer

class TaskRetriveAPIVieW(RetrieveAPIView):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer

class TaskUpdateAPIVieW(UpdateAPIView):
     queryset  = Tasks.objects.all()
     serializer_class = TaskUpdateSerializer

class TaskDestroyAPIVieW(DestroyAPIView):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer




class TaskListCreateAPIView(ListCreateAPIView):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer


class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer




# viewsets
class TaskViewSets(ModelViewSet):
     queryset = Tasks.objects.all()
     serializer_class = TaskSerializer