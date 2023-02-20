import random
from datetime import datetime

from django.utils.timezone import now

from some_app.models import Product


def create_product() -> None:
    start_time = datetime(
        year=2010,
        month=1,
        day=1,
        hour=0,
        minute=0,
        second=0,
    ).timestamp()

    tz = now().tzinfo

    product_objs = []
    count = 0
    for i in range(0, 5256000):
        product_objs.append(
            Product(
                low_price=random.uniform(1.0, 50.0),
                high_price=random.uniform(51.0, 100.0),
                demand_qty=random.randint(100, 1000),
                offers_qty=random.randint(1, 500),
                bought_qty=random.randint(1, 1000),
                sold_qty=random.randint(1, 1000),
                time_created=datetime.fromtimestamp(start_time + (i * 60), tz=tz),
            )
        )
        count += 1

        if count == 1000:
            Product.objects.bulk_create(objs=product_objs)

            count = 0
            product_objs = []

    return None
