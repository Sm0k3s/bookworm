from django.conf.urls import url
from books import views


urlpatterns = [
    url(r'^books/$', views.BookList.as_view(),
    name=views.BookList.name),
    url(r'^games/(?P<pk>[0-9]+)/$',
        views.BookDetail.as_view(),
        name=views.BookDetail.name),
]
