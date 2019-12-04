from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from api.models import Dish, Order
from api.serializers.others import DishSerializer


class Dishes(APIView):
    def get(self, request):
        serial = DishSerializer(Dish.objects.all(), many=True)
        return Response(serial.data)

    def post(self, request):
        data = json.loads(request.body)
        for dish in data['dishes']:
            id = dish['id']
            dish = Dish.objects.get(id=id)
            client = request.user
            Order.objects.create(client=client, dish=dish)
        return Response({"code": "0"})
    # def get(self, request):
    #     polls = Poll.objects.all().order_by('created_date')
    #     data = PollSerializer(polls, many=True).data
    #     return Response(data)
