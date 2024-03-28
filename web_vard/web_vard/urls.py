from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/user/', include('user.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('file/', include('file.urls')),
    path('access/', include('access.urls')),
    path('chart/', include('chart.urls')),
    path('feedback/', include('feedback.urls')),
]



