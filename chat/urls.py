from django.urls import path
from .views import homepageview,roomview
urlpatterns = [
    path('',homepageview),
    path('room/',roomview, name="room")

]