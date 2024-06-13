from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('api/accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('userprofile/', include('backend.urls'))
]
