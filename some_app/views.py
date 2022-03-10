from typing import List

from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from some_app.models import Product
from some_app.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    """4s place"""


class ProductGet(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = None

    def get(self, request, *args, **kwargs):
        """2d place"""
        # row_data = Product.objects.all()[:1e6]
        #
        # out_data = {
        #     'low_price': [],
        #     'high_price': [],
        #     'demand_qty': [],
        #     'offers_qty': [],
        #     'bought_qty': [],
        #     'sold_qty': [],
        #     'time_created': [],
        # }
        # for item in row_data:
        #     out_data['low_price'].append(item.low_price)
        #     out_data['high_price'].append(item.high_price)
        #     out_data['demand_qty'].append(item.demand_qty)
        #     out_data['offers_qty'].append(item.offers_qty)
        #     out_data['bought_qty'].append(item.bought_qty)
        #     out_data['sold_qty'].append(item.sold_qty)
        #     out_data['time_created'].append(item.time_created)

        """WINNER"""
        row_data: List[dict] = Product.objects.all()[:1e6].values()
        out_data = {
            'low_price': [],
            'high_price': [],
            'demand_qty': [],
            'offers_qty': [],
            'bought_qty': [],
            'sold_qty': [],
            'time_created': [],
        }
        for item in row_data:
            out_data['low_price'].append(item.get('low_price'))
            out_data['high_price'].append(item.get('high_price'))
            out_data['demand_qty'].append(item.get('demand_qty'))
            out_data['offers_qty'].append(item.get('offers_qty'))
            out_data['bought_qty'].append(item.get('bought_qty'))
            out_data['sold_qty'].append(item.get('sold_qty'))
            out_data['time_created'].append(item.get('time_created'))

        """3d place"""
        # out_data = Product.objects.all()[:1e6].values()

        return Response(data=out_data)
