from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ta_form$', views.ta_form, name='ta_form'),
    url(r'^contingent_form$', views.contingent_form, name='contingent_form')

]
