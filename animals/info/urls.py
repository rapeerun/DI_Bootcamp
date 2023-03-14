from django.urls import path
from . import views

urlpatterns = [
    path('family/<int:pk>/', views.family_detail, name='family_detail'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),
]