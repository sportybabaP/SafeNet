from django.urls import path
from safeNet1.views import sign_up

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),  # Sign up URL
]
