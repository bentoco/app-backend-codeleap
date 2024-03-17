# urls.py
from django.urls import path
from .views import CareerListCreateAPIView, CareerRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CareerListCreateAPIView.as_view(), name='career-list-create'),
    path('<int:pk>/', CareerRetrieveUpdateDestroyAPIView.as_view(), name='career-detail'),
]