from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView

from sso.user.views import ProfileView


urlpatterns = [
    # login view
    url(r'^accounts/login/$', LoginView.as_view(), name="login"),
    url(r'^accounts/logout/$', LogoutView.as_view(), name="logout"),
    # profile
    url(r'^accounts/profile/', ProfileView.as_view(), name="profile"),
]
