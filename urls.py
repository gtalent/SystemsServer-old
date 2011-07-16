from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Systems.views.home', name='home'),
    # url(r'^Systems/', include('Systems.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/(?P<postID>\d+)/$', 'posts.views.post'),
    url(r'^posts/$', 'posts.views.index'),
    url(r'^$', 'posts.views.index'),
)
