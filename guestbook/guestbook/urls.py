from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guestbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Links urls.py in gbook to main URLconf.
    url(r'^gbook/', include('gbook.urls', namespace="gbook")),
    url(r'^admin/', include(admin.site.urls)),
)
