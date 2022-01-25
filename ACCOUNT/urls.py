from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpUserView.as_view(), name='signup_user'),
    path('login/', views.LoginUserView.as_view(), name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('forgot-password/', views.ForgetPasswordRequestView.as_view(), name='forgot_pass_request'),
    path('forgot-password/success/', views.ForgetPasswordLinkSendView.as_view(), name='forgot_pass_mail_sent'),
    path('forget-password/new-password/<uidb64>/<token>/', views.ForgetPasswordChangePasswordView.as_view(), name='forget_pass_change'),
    path('forgot-password/complete/', views.ForgetPasswordSuccessView.as_view(), name='forget_password_success'),
]
