from django.conf.urls import url

from singelo.views import IndexView, PostView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1})/(?P<slug>[\w-]+)/$', PostView.as_view()),
]
