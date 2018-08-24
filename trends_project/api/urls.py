from django.urls import path

from .views import trend

urlpatterns = [
    path('start/', trend),
]
