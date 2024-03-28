from django.urls import path, include
from feedback.views import GetPostFeedbackAPIView, PutDeleteFeedbackAPIView


urlpatterns = [
    path('', GetPostFeedbackAPIView.as_view()),
    path('<int:pk>/', PutDeleteFeedbackAPIView.as_view()),
]