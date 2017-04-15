from django.conf.urls import url

from . import views

stock_urls = [
    # Detail for a single stock item
    url(r'^(?P<pk>[0-9]+)/?$', views.StockDetail.as_view(), name='stockitem-detail'),

    # List all stock items, with optional filters
    url(r'^\?.*/?$', views.StockList.as_view()),
    url(r'^$', views.StockList.as_view()),
]

stock_loc_urls = [
    url(r'^(?P<pk>[0-9]+)/?$', views.LocationDetail.as_view(), name='stocklocation-detail'),

    url(r'^\?.*/?$', views.LocationList.as_view()),

    url(r'^$', views.LocationList.as_view())
]

stock_track_urls = [
    url(r'^(?P<pk>[0-9]+)/?$', views.StockTrackingDetail.as_view(), name='stocktracking-detail'),

    url(r'^\?.*/?$', views.StockTrackingList.as_view()),

    url(r'^$', views.StockTrackingList.as_view())
]
