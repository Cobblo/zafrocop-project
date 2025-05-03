from django.urls import path
from . import views

urlpatterns = [
    path('', views.fake_admin, name='fake_admin'),
]
