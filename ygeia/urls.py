
from django.contrib import admin
from django.urls import path

from root_app import views as root_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_views.home, name='home'),
    path('about', root_views.about, name='about'),
]
