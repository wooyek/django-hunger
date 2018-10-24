from __future__ import unicode_literals
from django.urls import path, include
from django.views.generic import TemplateView

from . import views, always_allow_views

urlpatterns = (
    path('invited-only/', views.invited_only, name='invited_only'),
    path('always-allow/', views.always_allow, name='always_allow'),
    path('always-allow-module/', always_allow_views.allowed, name='always_allow_module'),
    path('not-allowed/', views.rejection, name='rejection'),
    path('hunger/', include('django_hunger2.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
)
