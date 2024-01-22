from django.urls import path

from bookshop.views import HomePageView, PublisherView, StoreListView, StoreDetialView, StoreCreateView, AuthorCreateView, AuthorDetialView, Author, AuthorListView

app_name = "bookshop"
urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("publisher/", PublisherView.as_view(), name="publisher-page"),
    path("stores/", StoreListView.as_view(), name="store-list"),
    path("stores/create", StoreCreateView.as_view(), name="store-create"),
    path("stores/<int:pk>", StoreDetialView.as_view(), name="store-detail"),
    path("author/", AuthorListView.as_view(), name="author-list"),
    path("author/create", AuthorCreateView.as_view(), name="author-create"),
    path("author/<int:pk>", AuthorDetialView.as_view(), name="author-detail"),
]
