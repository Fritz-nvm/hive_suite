from django.urls import path
from . import views

app_name= 'authentication'

urlpatterns = [
    path('', views.sign_up, name = 'sign_up'),
    path('login/', views.login, name = 'login')
    
]
