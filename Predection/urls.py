
from django.urls import path
from . import views


urlpatterns = [
    path('fifa', views.fifa),
    path('fifa/predict/', views.result,name='result'),
    path('diabetes', views.diabetes),
    path('diabetes/predict/', views.result_diabetes,name='result_diabetes'),
]