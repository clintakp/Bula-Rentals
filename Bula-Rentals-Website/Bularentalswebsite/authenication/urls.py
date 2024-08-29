from .views import RegistrationView, LoginView
from django.urls import path

urlpatterns = [
    path('signup', RegistrationView.as_view(), name="sign_up"),
    path('login', LoginView.as_view(), name="login")
]