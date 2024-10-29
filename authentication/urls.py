from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'authentication'


# urlpatterns = [
#     path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
# ]
urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
