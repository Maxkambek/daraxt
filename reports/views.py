from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .serializers import ReportSerializer
from .models import TreeReport
from trades.models import Trade
from contracts.models import Contract, ContractWithPartner
from trades.serializers import TradeSerializer
from contracts.serializers import ContractSerializer, ContractWithPartnerSerializer


class TreeReportCreateAPIView(generics.CreateAPIView):
    queryset = TreeReport.objects.all()
    serializer_class = ReportSerializer


class DocsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        trade = Trade.objects.all()
        contract = Contract.objects.all()
        report = TreeReport.objects.all()
        partner = ContractWithPartner.objects.all()
        partner_ser = ContractWithPartnerSerializer(partner, many=True).data
        trade_ser = TradeSerializer(trade, many=True).data
        contract_ser = ContractSerializer(contract, many=True).data
        report_ser = ReportSerializer(report, many=True).data
        return Response([trade_ser, contract_ser, report_ser, partner_ser], status=200)
