
from .views import *
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$',  index),
    url(r'^(\d+)$', show)
]
