from django.conf.urls import url, include
from books import views


urlpatterns = [
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^books/$', views.BookList.as_view(),
        name=views.BookList.name),
    url(r'^books/(?P<pk>[0-9]+)/$',
        views.BookDetail.as_view(),
        name=views.BookDetail.name),
    url(r'^book-categories/$', views.BookCategoryList.as_view(),
        name=views.BookCategoryList.name),
    url(r'^book-categories/(?P<pk>[0-9]+)/$',
        views.BookCategoryDetail.as_view(),
        name=views.BookCategoryDetail.name),
    url(r'^users/$',
        views.UserList.as_view(),
        name=views.UserList.name),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name=views.UserDetail.name),
]
