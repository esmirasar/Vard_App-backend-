from django.urls import path, include

from .views import GetPostCommentAPIView, DeletePutCommentAPIView


urlpatterns = [
    path('', GetPostCommentAPIView.as_view()),
    path('<int:pk>/', DeletePutCommentAPIView.as_view())
]
