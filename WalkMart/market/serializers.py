from rest_framework import serializers
from .models import WM_Market, WM_MarketPropertyDataElements, WM_MarketPropertyData


class WM_MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = WM_Market
        fields = ('ID', 'Name', 'DbName', 'ConnectionString')


class WM_MarketPropertyDataElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WM_MarketPropertyDataElements
        fields = ('PropertyID', 'PropertyName', 'Description')


class WM_MarketPropertyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WM_MarketPropertyData
        fields = ('PropertyDataID', 'PropertyID', 'PropertyValue')
