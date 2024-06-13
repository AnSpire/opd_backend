from django.urls import path
from .views import UserProfileDetailView

urlpatterns = [
    path('<str:username>/', UserProfileDetailView.as_view(), name='user-profile-detail'),
]
