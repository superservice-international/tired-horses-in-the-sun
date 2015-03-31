from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from nightvision_frontend.views import SliderView


urlpatterns = patterns('',
        url(r'^$', login_required(SliderView.as_view()), name="slider")
        )
