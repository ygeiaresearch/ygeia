
from django.contrib import admin
from django.urls import path, include

from root_app import views as root_views
from project_1 import views as project_1_views
from journal import views as journal_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.conf.urls.static import static
from django.conf import settings

#from journal.models import BlogPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('about', root_views.about, name='about'),
    path('projects', root_views.projects, name='projects'),
    path('project-1', project_1_views.home, name="project_1"),
    
    path('subscribe/', root_views.SubscriptionCreateView.as_view(), name="subscribe"),
    path('subscribe/success/', root_views.subscribe_success, name="subscribe_success"),
    
    path('journal/home/', journal_views.home, name="journal_home"),
    path('journal/page-type/<str:page_type>/', journal_views.page_type, name="journal_page_type"),

    path('journal/', include(wagtail_urls)),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)