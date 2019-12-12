from django.urls import path, include
from .views import *

urlpatterns = [
    path('', show_main, name="show_main"),
    path('bboard/', include('BBoard.urls')),
]
