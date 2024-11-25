from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home' ),
    path('new', views.new, name='page2'),
    path('next', views.new, name='page3'),
    path('futor', views.new, name='page4')

    ]