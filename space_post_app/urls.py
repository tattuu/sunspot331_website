from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^$', views.post_list, name='post_list'),
                  url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
                  url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
                  url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
                  url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
