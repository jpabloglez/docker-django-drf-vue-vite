from django.urls import path 
from analyses import views

# Define the urls
# A) tasks/ for tasks/ for fetching and adding tasks
# B) /tasks/<int:pk>/ for deleting and updating a task with a dynamic ID
urlpatterns = [
    path('analyses/', views.analyses),
    path('analyses/<int:pk>/', views.analyses_detail),
]