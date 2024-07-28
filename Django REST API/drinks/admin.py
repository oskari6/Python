#models not necessarly dont have to be here, just for convinience
from django.contrib import admin
from .models import Drink

admin.site.register(Drink)