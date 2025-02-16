from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Cookie, Order, OrderItem

def customer_list(request):
    customers = list(Customer.objects.values())
    return JsonResponse({'customers': customers})

def cookie_list(request):
    cookies = list(Cookie.objects.values())
    return JsonResponse({'cookies': cookies})

def order_list(request):
    orders = list(Order.objects.values())
    return JsonResponse({'orders': orders})
