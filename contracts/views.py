from typing import List

from django.core.files.uploadedfile import TemporaryUploadedFile
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.settings import api_settings
from accounts.permissions import IsTreeEkuvchi, IsTreeEktiruvchi
from .models import Contract, ContractWithPartner
from .serializers import ContractSerializer, ContractWithPartnerSerializer


class ContractCreateAPIView(generics.CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreeEkuvchi]
    authentication_classes = [TokenAuthentication]


class ContractWithPartnerCreateAPIView(generics.CreateAPIView):
    queryset = ContractWithPartner.objects.all()
    serializer_class = ContractWithPartnerSerializer
    permission_classes = [permissions.IsAuthenticated, IsTreeEktiruvchi]
    authentication_classes = [TokenAuthentication]
