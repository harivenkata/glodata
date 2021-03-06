from django.conf.urls.defaults import *
urlpatterns = patterns('feeds.views',
    (r'^$', 'view_all_feeds', {'all_feeds_template':'all_feeds_page.html'}, 'all_feeds'),
    (r'^search/$', 'view_search', {'search_template':'search.html'}, 'search'),
    (r'^(?P<feed_id>\d+)/$', 'view_feed_profile', {'feed_profile_template':'feed_profile.html'}, 'feed_profile'),
    (r'^(?P<feedentry_id>\d+)/(?P<feedentry_slug>[\w-]+)/$', 'view_feedentry_profile', {'feedentry_profile_template':'feedentry_profile.html'}, 'feedentry_profile'),
)