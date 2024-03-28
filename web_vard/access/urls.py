from django.urls import path

from access.views import GetPostAccessAPIView, PutDeleteAccessAPIView


urlpatterns = [
    path('', GetPostAccessAPIView.as_view()),
    path('<int:pk>/', PutDeleteAccessAPIView.as_view()),
]
