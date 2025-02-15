from django.contrib import admin
from .models import *

admin.site.register([Author, Book, User, Cart, Order, OrderDetail])