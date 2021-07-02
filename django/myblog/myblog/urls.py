from django.contrib import admin
from django.conf.urls import url
from blob.views import CityAutocomp

urlpatterns = [
    url(r'^city-autocomp/$', CityAutocomp.as_view(), name='city-autocomp'),
]
