from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^add_song$', views.add_song, name='add_song'),
    url(r'^view_songs$', views.view_songs, name='view_songs'),
    url(r'^edit_song$', views.edit_song, name='edit_song'),
    url(r'^delete_song$', views.delete_song, name='delete_song'),
    url(r'^add_collection$', views.add_collection, name='add_collection'),
    url(r'^view_collections$', views.view_collections, name='view_collections'),
    url(r'^edit_collection$', views.edit_collection, name='edit_collection'),
    url(r'^delete_collection$', views.delete_collection, name='delete_collection'),
    url(r'^view_lyrics', views.view_lyrics, name='view_lyrics'),
    url(r'^AHjEgvLdXWQGBFU', views.log_time, name='AHjEgvLdXWQGBFU'),
    url(r'^show_log_time', views.show_log_time, name='show_log_time'),
]
