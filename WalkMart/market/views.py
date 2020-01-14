from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WM_MarketSerializer, WM_MarketPropertyDataElementsSerializer, WM_MarketPropertyDataSerializer
from .models import WM_Market, WM_MarketPropertyDataElements, WM_MarketPropertyData
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from WalkMart import utility_belt

def get_market_data(market_id):
    market_data_res = request_market_data(market_id)
    return market_data_res[0]


def request_market_data(market_id):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = WM_Market.objects.filter(ID=market_id)
    serializer = WM_MarketSerializer(queryset,  many=True)
    return serializer.data


def map_market_data(market_data_response):
    res = {}
    for record in market_data_response:
        market_data = {}
        market_id = record.pop('ID')
        for name, value in record:
            market_data[name] = value
        res[market_id] = market_data
    return res


@api_view(['GET', 'POST'])
def market_details(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        request_body = json.loads(request.body)
        market_id = request_body['id']
        market_data = get_market_data(market_id)
        market_db = market_data.get('DbName')
        market_details = utility_belt.call_sproc( market_db, 'get_market_details', ())
        return Response(market_details)

    if request.method == 'POST':
        pass


def get_market_property_data_elements_objects(market_db):
    queryset = WM_MarketPropertyDataElements.objects.using(market_db).all()
    serializer = WM_MarketPropertyDataElementsSerializer(queryset, many=True)
    return serializer.data


def get_market_property_data(market_db):
    queryset = WM_MarketPropertyData.objects.using(market_db).all()
    serializer = WM_MarketPropertyDataSerializer(queryset, many=True)
    return serializer.data


def map_elements_to_data(prop_elements, prop_data):
    res = {}
    for record in prop_data:
        property_id = record.get('PropertyID')
        res[prop_elements.get(property_id)] = record.get('PropertyValue')
    return res


def get_ids_from_sql_data(sql_data):
    ids = []
    for record in sql_data:
        if record.get('PropertyID'):
            ids.append(record.get('PropertyID'))
    return ids


def get_prop_id_to_name_map(elemets_sql_response):
    res = {}
    for record in elemets_sql_response:
        res[record.get('PropertyID')] = record.get('PropertyName')
    return res

# def get_dict_from_ordered_dict(ordered_dict):
#     unordered_dict = {}
#     for item in ordered_dict:
#         unordered_dict.update(dict(item))
#     return unordered_dict

# class WM_MarketView(viewsets.ModelViewSet):
#     serializer_class = WM_MarketSerializer
#     print('My print statement')
#     queryset = WM_Market.objects.all()
