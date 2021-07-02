from django.conf.urls import url
from crudApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]