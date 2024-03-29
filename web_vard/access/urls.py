from django.urls import path

from access.views import GetPostAccessAPIView, PutDeleteAccessAPIView, ListAccessAPIView


urlpatterns = [
    path('all/', ListAccessAPIView.as_view()),
    path('<str:my_access>/', GetPostAccessAPIView.as_view()),
    path('<str:my_access>/<int:pk>/', PutDeleteAccessAPIView.as_view()),
]
