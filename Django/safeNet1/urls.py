from django.urls import path
from safeNet1 import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/', views.sign_up, name='sign_up'),  # Sign up URL
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact")
   
]
