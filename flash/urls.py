from django.urls import path
from .views import HomePageView

app_name = 'flash'

urlpatterns = [
    path('', HomePageView.as_view(), name='index')
]