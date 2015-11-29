from django.conf.urls import patterns, include, url
from supermarket import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', view=views.login),
    url(r'^supermarket/', include("djangosite.supermarket.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
