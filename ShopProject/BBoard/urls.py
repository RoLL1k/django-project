from django.urls import path
from .views import *

urlpatterns = [
    path('', show_bboard, name="show_bboard"),
    path('accounts/login/', BBoardLogin.as_view(), name="login"),
    path('accounts/profile/', profile, name="profile"),
    path('accounts/logout/', BBoardLogout.as_view(), name="logout")
]
