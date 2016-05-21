from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items$', views.index, name='index'),
    url(r'^items/(?P<item_id>[0-9]+)$', views.detail, name='details')
]
