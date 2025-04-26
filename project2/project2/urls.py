from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('Library/', include('Library.urls')),  # Include Library app URLs
]
