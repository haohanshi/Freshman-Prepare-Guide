from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='home'),
    url(r'^preface$', views.preface, name='preface'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^vpn$', views.vpn, name='vpn'),
    url(r'^checklist_1$', views.checklist_1, name='checklist_1'),
    url(r'^checklist_2$', views.checklist_2, name='checklist_2'),
    url(r'^at_school_1$', views.at_school_1, name='at_school_1'),
]