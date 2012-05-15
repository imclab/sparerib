from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "sparerib/index.html"

urlpatterns = patterns('',
    url(r'^agency/(?P<agency_id>[A-Z-]+$)', IndexView.as_view()),
    url(r'^docket/(?P<docket_id>[A-Z0-9-]+$)', IndexView.as_view()),
    url(r'^docket/(?P<docket_id>[A-Z0-9-]+)/clusters', IndexView.as_view()),
    url(r'^document/(?P<document_id>[A-Z0-9-]+$)', IndexView.as_view()),
    url(r'^(organization|individual|politician|entity)/[a-zA-Z0-9-]*/[a-z0-9-]+$', IndexView.as_view()),
    url(r'^search(-[a-z]+)?/(?P<query>.+$)', IndexView.as_view()),
    url(r'^$', IndexView.as_view())
)
