from django.urls import path
from . import views

app_name='playground'

urlpatterns=[
    path('Hello/', views.hello, name=('hello'))

]