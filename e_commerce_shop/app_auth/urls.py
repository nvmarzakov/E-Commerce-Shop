# app_auth/urls.py
from django.urls import path

from e_commerce_shop.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, UsersListView, \
    UserProfileDetailView, UserProfileEditView, UserProfileDeleteView, not_found_view

urlpatterns = (
    path('not-found/', not_found_view, name='not_found'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('profile-details/<int:pk>', UserProfileDetailView.as_view(), name='details_user'),
    path('edit-profile/<int:pk>', UserProfileEditView.as_view(), name='edit_user'),
    path('delete-profile/<int:pk>', UserProfileDeleteView.as_view(), name='delete_user'),
    path('', UsersListView.as_view(), name='user_list'),
)

# Marzakov85
