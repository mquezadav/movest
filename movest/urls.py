from django.conf.urls.defaults import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'movest.views.index'),
    url(r'timeline/', include('timeline.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

