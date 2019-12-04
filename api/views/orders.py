from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.models import Order, Dish, Restaurant
from api.serializers.others import OrdersSerializer


class Orders(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serial = OrdersSerializer(Order.objects.filter(client=request.user), many=True)
        return Response(serial.data)

    def post(self, request):
        try:
            data = json.loads(request.body)
            id = data['id']
            restaurant = Restaurant.objects.get(id=id)
            orders = Order.objects.filter(client=request.user, dish__restaurant=restaurant, is_done=False)
            for order in orders:
                order.is_done = True
                order.save()

            return Response({"code": "0", "purchased": str(len(orders)) + " dishes are bought"})
        except Exception as e:
            return Response({"code": "1", "error": str(e)})

