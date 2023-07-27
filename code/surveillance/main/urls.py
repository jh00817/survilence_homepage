from django.urls import path
from . import views # views 모듈에서 모든 기능을 import


urlpatterns = [
   path('login/', views.login, name='login'), # url 경로를 설정하는 방식

   path('', views.main, name='main'), 

   path('dev/', views.dev, name='dev'),
]