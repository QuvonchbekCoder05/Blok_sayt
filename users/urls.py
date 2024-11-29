from django.urls import path
from users.views import RegisterView, VerifyOTPView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='user-register'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('login/', LoginView.as_view(), name='user-login'),
]
