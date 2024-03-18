from django.urls import path
from app3 import views

#template urls

app_name='app3'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signup/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),

]