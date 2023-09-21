from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('validate_word/', views.validate_word, name='validate_word'),
]