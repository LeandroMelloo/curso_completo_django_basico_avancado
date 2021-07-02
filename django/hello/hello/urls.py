from django.contrib import admin
from django.conf.urls import url
from hello import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.hello)
]
