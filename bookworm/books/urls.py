from django.conf.urls import url
from books import views


urlpatterns = [
    url(r'^books/$', views.BookList.as_view(),
    name=views.BookList.name),
]
