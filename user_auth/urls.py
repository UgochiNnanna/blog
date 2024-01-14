from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", RegisterUser, name="sign_up"),
    path("signin/", LoginUser, name="sign_in"),
    path("signout/", LogoutUser, name="sign_out")
]