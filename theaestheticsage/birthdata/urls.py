from django.urls import path
from .views import BirthDataAPIView, AdjustGraphAPIView

urlpatterns = [
    path('', BirthDataAPIView.as_view(), name='birthdata'),
    path('adjust/', AdjustGraphAPIView.as_view(), name='adjust-graph'),
]
