from django.conf.urls import patterns, include, url
from .views import PostListView, PostDetailView

urlpatterns = patterns('',

    url(r'^posts/', PostListView.as_view()),
    url(r'^posts/(?P<post_id>\d+)', PostDetailView.as_view()),
)