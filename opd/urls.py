from backend import views
from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('example/', views.UserProfileViewSet.as_view({
        'get': 'list'  # Assuming you want to list resources when a GET request is made
    }), name='example'),
    path('api/accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
