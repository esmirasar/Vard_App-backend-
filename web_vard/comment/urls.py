from django.urls import path

from .views import GetPostCommentAPIView, DeletePutCommentAPIView, AllCommentAPIView, AllReadCommentAPIView


urlpatterns = [
    path('c-all/', AllCommentAPIView.as_view()),
    path('r-all/', AllReadCommentAPIView.as_view()),
    path('<str:comment>/', GetPostCommentAPIView.as_view()),
    path('<str:comment>/<int:pk>/', DeletePutCommentAPIView.as_view())
]
