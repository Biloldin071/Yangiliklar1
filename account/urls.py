from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, LogoutView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from .views import profil_view

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login' ),
    path('user-profil/', profil_view, name="user_profil"),
    path('logout/', LogoutView.as_view(), name="logout"),

    path('password-change/', PasswordChangeView.as_view(), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name="password_change_done"),

    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),


]
