from . import views
from django.urls import path

urlpatterns = [
    path('index',views.index),
    path('ft',views.formHttpText),
    path('time',views.dateTime),
]
