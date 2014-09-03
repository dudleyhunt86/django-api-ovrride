from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from commerceconnect import views


urlpatterns = patterns('',
    url(r'^$', 'commerceconnect.views.api_root', name='api-root'),
    url(r'^baskets/$', views.BasketList.as_view(), name='basket-list'),
    url(r'^baskets/(?P<pk>[0-9]+)/$', views.BasketDetail.as_view(), name='basket-detail'),
    url(r'^lines/$', views.LineList.as_view(), name='line-list'),
    url(r'^lines/(?P<pk>[0-9]+)/$', views.LineDetail.as_view(), name='line-detail'),
    url(r'^lineattributes/$', views.LineAttributeList.as_view(), name='lineattribute-list'),
    url(r'^lineattributes/(?P<pk>[0-9]+)/$', views.LineAttributeDetail.as_view(), name='lineattribute-detail'),
    url(r'^products/$', views.ProductList.as_view(), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view(), name='product-detail'),
    url(r'^stockrecords/$', views.StockRecordList.as_view(), name='stockrecord-list'),
    url(r'^stockrecords/(?P<pk>[0-9]+)/$', views.StockRecordDetail.as_view(), name='stockrecord-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)