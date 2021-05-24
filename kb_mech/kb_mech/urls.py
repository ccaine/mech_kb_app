from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('groupbuys/', include('groupbuys.urls')),
    path('admin/', admin.site.urls),
]