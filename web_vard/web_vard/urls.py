from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/user/', include('user.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/dashboard/', include('dashboard.urls')),
    path('api/file/', include('file.urls')),
    path('api/access/', include('access.urls')),
    path('api/chart/', include('chart.urls')),
    path('api/feedback/', include('feedback.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')

]



