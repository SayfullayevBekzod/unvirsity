from django.urls import path

from bookshop.views import HomePageView, PublisherView, StoreListView, StoreDetialView, StoreCreateView, \
    UserRegisterView, UserLoginView, UserLogoutView

app_name = "bookshop"
urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView, name="login"),
    path("logout/", UserLogoutView, name="logout"),
    path("publisher/", PublisherView.as_view(), name="publisher-page"),
    path("stores/", StoreListView.as_view(), name="store-list"),
    path("stores/create", StoreCreateView.as_view(), name="store-create"),
    path("stores/<int:pk>", StoreDetialView.as_view(), name="store-detail"),
]
