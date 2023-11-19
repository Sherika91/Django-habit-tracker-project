from django.urls import path

from .apps import HabitConfig
from . import views

app_name = HabitConfig.name

urlpatterns = [
    path('habit/create/', views.HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/list/', views.HabitListAPIView.as_view(), name='habit-list'),
    path('habit/public/list/', views.PublicHabitListAPIView.as_view(), name='public-habit-list'),
    path('habit/<int:pk>/', views.HabitUpdateRetrieveDestroyAPIView.as_view(), name='habit-detail'),

]
