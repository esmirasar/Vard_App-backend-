from django.urls import path

from .views import ShowListUserAPIView, GetUserAPIView


urlpatterns = [
    path('', ShowListUserAPIView.as_view()),
    path('me/', GetUserAPIView.as_view()),
]
