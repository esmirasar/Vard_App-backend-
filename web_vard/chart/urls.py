from django.urls import path
from chart.views import GetPostChartAPIView, PutDeleteChartAPIView, ListChartAPIView


urlpatterns = [
    path('all/', ListChartAPIView.as_view()),
    path('<str:my_chart>/', GetPostChartAPIView.as_view()),
    path('<str:my_chart>/<int:pk>/', PutDeleteChartAPIView.as_view()),
]
