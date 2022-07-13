from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('portfolio/', include('Portfolio.urls')),
    path('admin/', admin.site.urls),
]