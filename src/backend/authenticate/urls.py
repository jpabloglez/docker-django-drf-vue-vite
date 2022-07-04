from django.urls import path 
from .views import UserAPIView

# Define the urls
# A) tasks/ for tasks/ for fetching and adding tasks
# B) /tasks/<int:pk>/ for deleting and updating a task with a dynamic ID
urlpatterns = [
    path('users/', UserAPIView.as_view()),
]