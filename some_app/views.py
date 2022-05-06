from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from some_app.models import Product
from some_app.serializers import ProductSerializer

LIMIT_100 = int(1e2)
LIMIT_1K = int(1e3)
LIMIT_10K = int(1e4)
LIMIT_100K = int(1e5)
LIMIT_1M = int(1e6)


class ProductViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.all()[:LIMIT_1K]
    """ V1    3 RPS """


class ProductsValuesViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ProductSerializer
    queryset = Product.objects.values()[:LIMIT_1K]
    """ V2 """


class ProductsValues(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        """ V3    4.8 RPS """
        return Response(data=Product.objects.values()[:LIMIT_1K])


# @login_required
# @permission_required(perm, login_url=None, raise_exception=False)
def products_values(request, *args, **kwargs):
    """ V3.2; +5-10% time of v.3; can NOT do 1M. """
    return JsonResponse(data=list(Product.objects.values()[:LIMIT_1M]), safe=False)


class ForLoopObjects(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        """ V4 """
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
        """ V5 """
        out_data = {
            'low_price': [],
            'high_price': [],
            'demand_qty': [],
            'offers_qty': [],
            'bought_qty': [],
            'sold_qty': [],
            'time_created': [],
        }
        for item in Product.objects.values()[:LIMIT_1K]:
            out_data['low_price'].append(item.get('low_price'))
            out_data['high_price'].append(item.get('high_price'))
            out_data['demand_qty'].append(item.get('demand_qty'))
            out_data['offers_qty'].append(item.get('offers_qty'))
            out_data['bought_qty'].append(item.get('bought_qty'))
            out_data['sold_qty'].append(item.get('sold_qty'))
            out_data['time_created'].append(item.get('time_created'))

        return Response(data=out_data)


class SQLDebugV1(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        out_data = {
            'low_price': [],
            'high_price': [],
        }

        """ v1: 4.8 RPS; SQL: 1q ~550ms """
        # products = Product.objects.all()[:LIMIT_100]
        # for product in products:
        #     out_data['low_price'].append(product.low_price)
        #     out_data['high_price'].append(product.high_price)

        """ v2: 5.8 RPS, +17%; SQL: 1q ~435ms """
        # products = Product.objects.only(
        #     'low_price',
        #     'high_price'
        # )[:LIMIT_100]
        # for product in products:
        #     out_data['low_price'].append(product.low_price)
        #     out_data['high_price'].append(product.high_price)

        """ v3: rq: 440ms; 6.3 RPS, +8% (total +25%); SQL: 1q ~405ms """
        products = Product.objects.values(
            'low_price',
            'high_price',
        )[:LIMIT_100]
        for product in products:
            out_data['low_price'].append(product.get('low_price'))
            out_data['high_price'].append(product.get('high_price'))

        return Response(data=out_data)


class SQLDebugV2(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        out_data = {
            'low_price': [],
            'high_price': [],
        }

        """ 5.5 RPS; SQL: 101q ~450ms """
        products = Product.objects.only(
            'low_price',
        )[:LIMIT_100]

        for product in products:
            out_data['low_price'].append(product.low_price)
            out_data['high_price'].append(product.high_price)

        return Response(data=out_data)


class SQLDebugV3(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, *args, **kwargs):
        out_data = {
            'low_price': [],
            'high_price': [],
        }

        """ rq: 5ms; 900 RPS; SQL: 0q 0ms """
        products = Product.objects.all()

        return Response(data=out_data)
