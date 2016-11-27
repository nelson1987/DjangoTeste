"""
Definition of urls for TesteDjango.
"""

from datetime import datetime
from django.conf.urls import *
from app.forms import BootstrapAuthenticationForm
from app import views
#from django.contrib import auth
#import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^contact$', views.contact, name="contact"),
    url(r'^about', views.about, name='about')
]

#urlpatterns = patterns('',
#    url(r'^about/([0-9]{4})/$', 'year_archive'),
    
#    # Examples:
#    #url(r'^$', 'app.views.home', name='home'),
#    #url(r'^contact$', 'app.views.contact', name='contact'),
#    #url(r'^about', 'app.views.about', name='about'),
#    #url(r'^login/$',
#    #    'django.contrib.auth.views.login',
#    #    {
#    #        'template_name': 'app/login.html',
#    #        'authentication_form': BootstrapAuthenticationForm,
#    #        'extra_context':
#    #        {
#    #            'title':'Log in',
#    #            'year':datetime.now().year,
#    #        }
#    #    },
#    #    name='login'),
#    #url(r'^logout$',
#    #    'django.contrib.auth.views.logout',
#    #    {
#    #        'next_page': '/',
#    #    },
#    #    name='logout'),

#    # Uncomment the admin/doc line below to enable admin documentation:
#    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#    # Uncomment the next line to enable the admin:
#    # url(r'^admin/', include(admin.site.urls)),
#)
