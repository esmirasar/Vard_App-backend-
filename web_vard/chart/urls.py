from django.urls import path
from chart.views import GetPostChartAPIView, PutDeleteChartAPIView


urlpatterns = [
    path('', GetPostChartAPIView.as_view()),
    path('<int:pk>/', PutDeleteChartAPIView.as_view()),
]
