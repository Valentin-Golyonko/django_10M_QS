from rest_framework import serializers

from some_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'low_price',
            'high_price',
            'demand_qty',
            'offers_qty',
            'bought_qty',
            'sold_qty',
            'time_created',
        )
