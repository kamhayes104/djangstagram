from django.urls import path, include
from .views import profile_list_view, profile_detail, sign_up, complete_profile, confirm_profile, edit_user

urlpatterns = [
    path('profiles/', profile_list_view, name='profile_list_view'),
    path('profile/<int:pk>', profile_detail, name='profile_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign_up', sign_up, name='sign_up'),
    path('account/edit', edit_user, name='edit_user'),
    path('account/complete/<int:pk>', complete_profile, name='complete_profile'),
    path('account/confirm', confirm_profile, name='confirm_profile'),
]
