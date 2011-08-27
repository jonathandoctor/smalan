from django.conf.urls.defaults import *

urlpatterns = patterns('smalan.main.views',
    # Main app
    (r'^$', 'main'),

    (r'^test/$', 'test'),
)

