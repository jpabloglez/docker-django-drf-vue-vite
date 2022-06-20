from django.urls import path 
from tasks import views

# Define the urls
# A) tasks/ for tasks/ for fetching and adding tasks
# B) /tasks/<int:pk>/ for deleting and updating a task with a dynamic ID
urlpatterns = [
    path('tasks/', views.tasks),
    path('tasks/<int:pk>/', views.task_detail),
]