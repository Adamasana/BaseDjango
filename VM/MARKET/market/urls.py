from django.urls import path
from market.views import home

urlpatterns = [
    path('', home),
]