from django.conf.urls import patterns, include, url
from pinata.models import Page

urlpatterns = patterns('pinata.views',

	url(r'^$', 'page_view'),
	url(r'^[0-9a-zA-Z_-]+/$', 'page_view'),

)