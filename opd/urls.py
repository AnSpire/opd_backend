from backend import views
from django.urls import path

urlpatterns = [
    path('example/', views.UserProfileViewSet.as_view({
        'get': 'list'  # Assuming you want to list resources when a GET request is made
    }), name='example'),
]
