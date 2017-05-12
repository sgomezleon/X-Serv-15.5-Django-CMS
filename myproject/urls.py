from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^(.+)', views.numero_pagina, name='pagina de usuario'),
	url(r'^', views.home, name='Pagina principal'),

)
