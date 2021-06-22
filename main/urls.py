from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('another_one/<str:name>', views.another),
    path('hello', views.hello),
    path('redirected', views.redirected),
    path('complete_redirect', views.complete),
    path('<urls>', views.catch_all)
]
