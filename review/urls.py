"""review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from posts import views as posts_views
from review import views as review_views
from posts import regbackend

urlpatterns = [
    url(r'^$', posts_views.home, name='home'),
    url(r'^refer/$', posts_views.refer, name='refer'),
    url(r'^about/$', review_views.about, name='about'),
    url(r'^create/$', posts_views.post_create, name='create'),
    #url(r'^search/$', posts_views.post_search, name='search'),
    url(r'^recent/$', posts_views.post_list, name='recent'),
    url(r'^review/(?P<id>\d+)/$', posts_views.post_detail, name='detail'),
    #url(r'^signup/$', 'newsletter.views.signup', name='signup'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', regbackend.MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^sitemap/', posts_views.sitemap, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)