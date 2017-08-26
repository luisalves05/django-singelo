from django.conf.urls import url

from singelo.views import Index

urlpatterns = [
    url(r'^$', Index.as_view()),
]
