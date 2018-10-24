import registration
from django.urls import path, include

from django.contrib import admin

from . import views

urlpatterns = (
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.home, name='home'),
    path('hunger/', include('hunger.urls')),
    path('accounts/profile/', views.profile, name='profile'),
)
