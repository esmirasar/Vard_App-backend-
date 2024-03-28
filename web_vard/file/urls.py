from django.urls import path, include
from file.views import GetPostFileAPIView, PutDeleteAPIView


urlpatterns = [
    path('', GetPostFileAPIView.as_view()),
    path('<int:pk>/', PutDeleteAPIView.as_view()),
]