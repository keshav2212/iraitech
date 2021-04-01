from django.urls import path
from api import views
urlpatterns = [
    path('v1/calculate',views.calculate,name='calculate'),
    path('login',views.login1,name='login'),
    path('',views.home)
]
