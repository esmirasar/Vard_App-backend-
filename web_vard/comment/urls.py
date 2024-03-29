from django.urls import path

from .views import (GetPostCommentAPIView, DeletePutCommentAPIView, AllCommentAPIView,
                    AllReadCommentAPIView, GetPostReadCommentAPIView, PutDeleteReadCommentAPIView)


urlpatterns = [
    path('c-all/', AllCommentAPIView.as_view()),
    path('r-all/', AllReadCommentAPIView.as_view()),

    path('<str:my_comment>/', GetPostCommentAPIView.as_view()),
    path('<str:my_comment>/<int:pk>/', DeletePutCommentAPIView.as_view()),

    path('<str:my_readcomment>/', GetPostReadCommentAPIView.as_view()),
    path('<str:my_readcomment>/<int:pk>/', PutDeleteReadCommentAPIView.as_view())
]
