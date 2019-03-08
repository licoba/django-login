
from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('login_check', views.login_check),
    path('test_ajax', views.test_ajax),
    path('ajax_handle', views.ajax_handle),
    path('login_ajax', views.login_ajax),
    path('login_ajax_check', views.login_ajax_check),
]