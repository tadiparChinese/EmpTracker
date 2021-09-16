from authentication.views import RegisterAPI
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    # path('api/user/', UserAPIView.as_view()),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', LogoutView.as_view(), name='logout'),
    # path('api/info/', EmployeeInfoAPI.as_view(), name= 'employeeinfo'),
]
