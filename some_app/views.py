from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from some_app.models import Product
from some_app.serializers import ProductSerializer

LIMIT_1K = 1e3
LIMIT_10K = 1e4
LIMIT_100K = 1e5
LIMIT_1M = 1e6


class ProductViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:LIMIT_1K]
    """ 5s place """


class ProductsValuesViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:LIMIT_1K].values()
    """ 4s place """


class ProductsValues(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        """ 3d place """
        return Response(data=Product.objects.all()[:LIMIT_1K].values())


class ForLoopObjects(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        """ 2d place """
        out_data = {
            'low_price': [],
            'high_price': [],
            'demand_qty': [],
            'offers_qty': [],
            'bought_qty': [],
            'sold_qty': [],
            'time_created': [],
        }
        for item in Product.objects.all()[:LIMIT_1K]:
            out_data['low_price'].append(item.low_price)
            out_data['high_price'].append(item.high_price)
            out_data['demand_qty'].append(item.demand_qty)
            out_data['offers_qty'].append(item.offers_qty)
            out_data['bought_qty'].append(item.bought_qty)
            out_data['sold_qty'].append(item.sold_qty)
            out_data['time_created'].append(item.time_created)

        return Response(data=out_data)


class ForLoopValues(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        """ WINNER """
        out_data = {
            'low_price': [],
            'high_price': [],
            'demand_qty': [],
            'offers_qty': [],
            'bought_qty': [],
            'sold_qty': [],
            'time_created': [],
        }
        for item in Product.objects.all()[:LIMIT_1K].values():
            out_data['low_price'].append(item.get('low_price'))
            out_data['high_price'].append(item.get('high_price'))
            out_data['demand_qty'].append(item.get('demand_qty'))
            out_data['offers_qty'].append(item.get('offers_qty'))
            out_data['bought_qty'].append(item.get('bought_qty'))
            out_data['sold_qty'].append(item.get('sold_qty'))
            out_data['time_created'].append(item.get('time_created'))

        return Response(data=out_data)


class V6(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        return Response(data=Product.objects.values()[:LIMIT_1K])
