﻿"""
Definition of urls for TesteDjango.
"""

from datetime import datetime
from django.conf.urls import *
from app.forms import BootstrapAuthenticationForm
from django.contrib.auth import views
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^contact$', app.views.contact, name="contact"),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
