from rest_framework import generics
from .serializers import ReportSerializer
from .models import TreeReport


class TreeReportCreateAPIView(generics.CreateAPIView):
    queryset = TreeReport.objects.all()
    serializer_class = ReportSerializer
