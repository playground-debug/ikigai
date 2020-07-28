from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signupuser, name="signupuser"),
    path('logout', views.logoutuser, name="logoutuser"),
    path('login', views.loginuser, name="loginuser"),
    path('show/<int:profile_id>', views.show, name="show"),
    path('create', views.create, name="create"),
]
