
from django.contrib import admin
from django.urls import path

from root_app import views as root_views
from project_1 import views as project_1_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_views.home, name='home'),
    path('about', root_views.about, name='about'),
    path('projects', root_views.projects, name='projects'),
    path('project-1', project_1_views.home, name="project_1")
]
