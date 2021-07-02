from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include 
from crudApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crudApp/', include('crudApp.urls')),
    url(r'^admin/', admin.site.urls),
]
