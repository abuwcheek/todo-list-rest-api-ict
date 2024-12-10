from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tasks
          fields = ('title', 'task_time', 'complete', 'created', 'updated')

     
class TaskUpdateSerializer(serializers.ModelSerializer):
     class Meta:
          model = Tasks
          fields = ('complete',)