# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from search import views

urlpatterns = patterns('',
    # URL pattern for the UserDetailView
    url(
        regex=r'^$',
        view=TemplateView.as_view(template_name="search/search_main.html"),
        name='main'
    ),
)
