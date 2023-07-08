from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
]

