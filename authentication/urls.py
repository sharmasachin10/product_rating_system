from django.urls import path, include

from authentication.views import RegisterAPI, UserLogin

urlpatterns = [
    path('register/',RegisterAPI.as_view(),name='registration' ),
    path('login/',UserLogin.as_view(),name = 'login'),
 ]