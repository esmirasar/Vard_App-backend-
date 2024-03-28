from django.urls import path, include

from .views import *


urlpatterns = [
    path('', ShowListUserAPIView.as_view()),
    path('me/', GetUserAPIView.as_view()),
]
