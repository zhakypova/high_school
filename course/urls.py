
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('programing.urls')),
    path('', include('high_school.urls')),
]
