# app_auth/urls.py
from django.urls import path

from e_commerce_shop.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, UsersListView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('', UsersListView.as_view(), name='users_list'),
)

# Marzakov85