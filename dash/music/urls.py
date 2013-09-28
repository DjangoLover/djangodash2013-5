# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from music import views

urlpatterns = patterns('',
    # URL pattern for the UserDetailView
    url(
        regex=r'^$',
        view=views.MusicProfileDetailView.as_view(),
        name='detail'
    ),
    # URL pattern for the UserDetailView
    url(
        regex=r'update/$',
        view=views.MusicProfileUpdateView.as_view(),
        name='update'
    ),
)
