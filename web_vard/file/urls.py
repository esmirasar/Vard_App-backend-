from django.urls import path
from file.views import FileAPIView, ShowListFileAPIView, PutDeleteAPIView


urlpatterns = [
    path('all/', ShowListFileAPIView.as_view()),
    path('<str:my_files>/', FileAPIView.as_view()),
    path('<str:my_files>/<int:pk>/', PutDeleteAPIView.as_view())
]
