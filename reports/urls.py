from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.TreeReportCreateAPIView.as_view())
]
