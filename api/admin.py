from django.contrib import admin

# Register your models here.
from api.models import MainUser, Dish, Restaurant, Order

admin.site.register(MainUser)
admin.site.register(Dish)
admin.site.register(Restaurant)
admin.site.register(Order)

