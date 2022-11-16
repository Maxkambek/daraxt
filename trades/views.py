from rest_framework import generics
from .models import Region, District, TreeClassifier, TypeTree, TreeDeliveryCompany, Trade
from .serializers import RegionSerializer, DistrictSerializer, TreeTypeSerializer, TreeClassifierSerializer, \
    TreeDeliveryCompanySerializer, TradeSerializer


class RegionListAPIView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictListAPIView(generics.ListAPIView):
    serializer_class = DistrictSerializer

    def get_queryset(self):
        queryset = District.objects.all()
        pk = self.request.GET.get('region_id')
        if pk:
            queryset = queryset.filter(region_id=pk)
        return queryset


class TreeClassifierListAPIView(generics.ListAPIView):
    queryset = TreeClassifier.objects.all()
    serializer_class = TreeClassifierSerializer


class TypeTreeListAPIView(generics.ListAPIView):
    serializer_class = TreeTypeSerializer

    def get_queryset(self):
        queryset = TypeTree.objects.all()
        pk = self.request.GET.get('classifier_id')
        if pk:
            queryset = queryset.filter(classifier_id=pk)
        return queryset


class TreeDeliveryListAPIView(generics.ListAPIView):
    serializer_class = TreeDeliveryCompanySerializer

    def get_queryset(self):
        queryset = TreeDeliveryCompany.objects.all()
        pk = self.request.GET.get('region_id')
        if pk:
            queryset = queryset.filter(address_id=pk)
        return queryset


class TradeCreateAPIView(generics.CreateAPIView):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

