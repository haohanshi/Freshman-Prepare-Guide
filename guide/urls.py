from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='home'),
    url(r'^preface$', views.preface, name='preface'),
]