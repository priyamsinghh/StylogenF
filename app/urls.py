from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('testView/', HomeView.as_view(), name='testView'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("text2image/", TextToImageView.as_view(), name="text-to-image"),
    path('userhistory/', UserHistoryListView.as_view(), name='user-history'),
    path('deletecontext/', ResetContextListView.as_view(),name='deletecontext'),
]
