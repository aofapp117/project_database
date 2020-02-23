from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('666', views.index2, name='index2'),
    path('test', views.test, name='test')

]