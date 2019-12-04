from django.db import models
from api.models.user import MainUser


class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    admin = models.ForeignKey(MainUser, on_delete=models.CASCADE, null=False)
    location = models.CharField(max_length=250, blank=False, null=False)
    image = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Dish(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False)
    image = models.CharField(max_length=250, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)


class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.DO_NOTHING, null=False)
    client = models.ForeignKey(MainUser, on_delete=models.DO_NOTHING, null=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {}'.format(self.id, self.client)




