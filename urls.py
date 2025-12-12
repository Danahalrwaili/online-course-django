from django.urls import path
from courses import views
urlpatterns = [
 path('', views.index),
 path('course/1/exam/', views.exam),
 path('course/1/result/', views.result),
]
