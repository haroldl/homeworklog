from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^$', 'log.views.index'),
    ('^submit$', 'log.views.submit'),
    ('^thanks/(?P<first_name>.*)$', 'log.views.thanks'),
    ('^log.css$', 'log.views.css'),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),
)
