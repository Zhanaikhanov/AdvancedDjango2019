from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView

from api.models import Restaurant
from api.serializers.others import RestaurantSerializer


class Restaurants(ListCreateAPIView):
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Restaurant.objects.all()
