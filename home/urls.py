from django.urls import path
from rest_framework import routers
from .views import (
     # TaskView,
     # TaskRetriveAPIView, 
     TaskListAPIVieW,
     TaskCreateAPIVieW,
     TaskRetriveAPIVieW,
     TaskUpdateAPIVieW,
     TaskDestroyAPIVieW,
     TaskListCreateAPIView, 
     TaskRetrieveUpdateDestroyAPIView, 
     TaskViewSets
)


router = routers.DefaultRouter()
router.register('task', TaskViewSets, basename='task')


urlpatterns = [
     # path('tasks', TaskView.as_view(), name="task-list"),
     # path('tasks/<int:pk>', TaskRetriveAPIView.as_view(), name="task-retrive "),



     # path('tasks', TaskListAPIVieW.as_view(),),
     # path('tasks-create', TaskCreateAPIVieW.as_view(),),
     # path('tasks-retrive/<int:pk>', TaskRetriveAPIVieW.as_view(),),
     # path('tasks-update/<int:pk>', TaskUpdateAPIVieW.as_view(),),
     # path('tasks-delete/<int:pk>', TaskDestroyAPIVieW.as_view(),),


     # path('tasks', TaskListCreateAPIView.as_view()),
     # path('task/<int:pk>', TaskRetrieveUpdateDestroyAPIView.as_view())
]

urlpatterns += router.urls