from django.urls import path

from accounts.views import SignUpView, SignInView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('signin/', SignInView.as_view())
]
