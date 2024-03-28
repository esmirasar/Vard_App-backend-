from django.urls import path

from .views import GetPostCommentAPIView, DeletePutCommentAPIView


urlpatterns = [
    path('', GetPostCommentAPIView.as_view()),
    path('<int:pk>/', DeletePutCommentAPIView.as_view())
]
