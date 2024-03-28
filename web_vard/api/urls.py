from django.urls import path

from api.local_db.connection import ConnectDBAPIView

from .views import (UserAPIView, FileAPIView, AccessAPIView, FeedbackAPIView,
                    ChartAPIView, DashboardAPIView, CommentAPIView, ReadCommentAPIView)


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('file/', FileAPIView.as_view()),
    path('file/<int:pk>/', FileAPIView.as_view()),
    path('dashboard/', DashboardAPIView.as_view()),
    path('dashboard/<int:pk>/', DashboardAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>/', CommentAPIView.as_view()),
    path('read_comment/', ReadCommentAPIView.as_view()),
    path('read_comment/<int:pk>/', ReadCommentAPIView.as_view()),
    path('access/', AccessAPIView.as_view()),
    path('access/<int:pk>/', AccessAPIView.as_view()),
    path('feedback/', FeedbackAPIView.as_view()),
    path('feedback/<int:pk>/', FeedbackAPIView.as_view()),
    path('chart/', ChartAPIView.as_view()),
    path('chart/<int:pk>/', ChartAPIView.as_view()),
    path('connection/', ConnectDBAPIView.as_view())
]
