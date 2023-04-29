from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz_dog_3/', views.quiz_dog_3, name='quiz_dog_3'),
    path('quiz_dog_4/', views.quiz_dog_4, name='quiz_dog_4'),
    path('quiz_dog_5/', views.quiz_dog_5, name='quiz_dog_5'),
    path('test_result_dog/', views.test_result_dog, name='test_result_dog'),
]