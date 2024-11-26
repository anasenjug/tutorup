from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_student, name='register_student'),
    path('registration-success/', views.registration_success, name='registration_success'),
]
