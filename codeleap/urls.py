
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("careers/", include("careers.urls")),
    path('admin/', admin.site.urls),
]
