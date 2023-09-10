from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.LoginView.as_view()),
    path('api/signup', views.RegisterView.as_view()),
    path('api/login', views.LoginView.as_view()),
    path('api/trains/create', views.TrainView.as_view()),
]
