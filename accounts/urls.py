from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordResetDoneView

app_name = "accounts"
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password_reset/', views.PasswordReset.as_view(), name="password_reset"),
    path('password_reset/done/', views.PasswordResetDone.as_view(),
         name="password_reset_done"),
    path("confirm/<uidb64>/<token>/", views.PasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path("password_reset/complete/", views.PasswordResetComplete.as_view(), name="password_reset_complete")
]
