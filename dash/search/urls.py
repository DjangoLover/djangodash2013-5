# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from search import views

urlpatterns = patterns('',
    # URL pattern for the UserDetailView
    url(
        regex=r'^$',
        view=views.main_search_form,
        name='main'
    ),
)
