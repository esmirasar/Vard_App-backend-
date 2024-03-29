from django.urls import path
from feedback.views import GetPostFeedbackAPIView, PutDeleteFeedbackAPIView, AllFeedbackAPIView


urlpatterns = [
    path('all/', AllFeedbackAPIView.as_view()),
    path('<str:my_feedback>/', GetPostFeedbackAPIView.as_view()),
    path('<str:my_feedback>/<int:pk>/', PutDeleteFeedbackAPIView.as_view()),
]
