from django.conf.urls.defaults import *
from Atom2RETS.views import LatestEntries

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

feeds = {
    'Translator': LatestEntries,
}


urlpatterns = patterns('',
    (r'^(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

