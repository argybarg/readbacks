from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(
        r'^unit/$',
        TemplateView.as_view(template_name="reader/unit.html"),
        name="home"
    )
)
