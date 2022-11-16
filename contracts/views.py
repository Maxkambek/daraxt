from rest_framework import generics
from .models import Contract, ContractWithPartner
from .serializers import ContractSerializer, ContractWithPartnerSerializer


class ContractCreateAPIView(generics.CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractWithPartnerCreateAPIView(generics.CreateAPIView):
    queryset = ContractWithPartner.objects.all()
    serializer_class = ContractWithPartnerSerializer
