from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view()),
    path('login/', LoginView.as_view(), name="login"),
    path('sign-up/', SignUpView.as_view(), name="sign_up"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
