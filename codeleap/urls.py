from django.urls import include, path

urlpatterns = [
    path("careers/", include("careers.urls"))
]
