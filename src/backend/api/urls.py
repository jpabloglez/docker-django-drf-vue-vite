from django.urls import path

from .views import LoginView, SessionView

urlpatterns = [
    path('login/', LoginView.as_view(), name='api-login'),
    # path('logout/', views.logout_view, name='api-logout'),
    path('session/', SessionView.as_view(), name='api-session'),
    # path('whoami/', views.whoami_view, name='api-whoami'),
]