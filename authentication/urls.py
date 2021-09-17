from authentication.views import RegisterAPI, LoginAPI, AuthUserAPI
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('user/', AuthUserAPI.as_view(), name='user'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/logout/', LogoutView.as_view(), name='logout'),
    # path('api/info/', EmployeeInfoAPI.as_view(), name= 'employeeinfo'),
]
