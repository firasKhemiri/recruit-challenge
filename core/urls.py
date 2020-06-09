"""This module contains the routing for the templates that will get its data from the API using JS"""
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^customers/$', TemplateView.as_view(template_name='all_customers.html')),
    url(r'^customer/(?P<pk>[0-9]+)/$',  TemplateView.as_view(template_name='single_customer.html')),
]


