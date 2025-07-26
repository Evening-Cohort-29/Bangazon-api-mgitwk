from django.shortcuts import render
from bangazonapi.models import Order
from django.db.models import Sum, F


def incomplete_orders_report(request):

    # currently in urls.py we have a route to reports/orders, but we want below this report to route to reports/orders?status=incomplete
    # only show the report if the query param status=incomplete
    status = request.GET.get("status")
    if status == "incomplete":

        # use django ORM and annotate to get all unpaid orders and total product cost

        orders = (
            # annotate let's you add calculated fields to each obj in a query set
            Order.objects.filter(payment_type__isnull=True).annotate(
                # F() let's you refer to model fields directly in a query
                # lineitems is the related name on the orderproduct join table model
                # For each of the unpaid orders, calculate the sum of the price of each product referenced in a related lineitem (OrderProduct) row, and annotate the order with this value as a new field called total_cost
                total_cost=Sum(F("lineitems__product__price"))
            )
        )

    # set the data up for use in our template
        data = []
        for order in orders:
            data.append({
                "order_id": order.id,
                "customer_name": f"{order.customer.user.first_name} {order.customer.user.last_name}",                "total_cost": f"${order.total_cost:.2f}"
            })

        # use the render fx from django's shortcuts module to render the incomplete_orders.html template with the orders dictionary
        return render(request, 'reports/incomplete_orders.html', {"orders": data})
