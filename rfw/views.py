from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from rest_framework import generics
from .serializers import *
from rest_framework import viewsets


@csrf_exempt
def create_goods(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_goods = Goods.objects.create(**data)
        json_data = {
            'name': new_goods.name,
            'price': new_goods.price,
            'label': new_goods.label,
            'category': new_goods.category,
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        goods = Goods.objects.all()
        data = []
        for good in goods:
            data.append(
                {
                    'name': good.name,
                    'price': good.price,
                    'label': good.label,
                    'category': good.category,
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_label(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_goods = Label.objects.create(**data)
        json_data = {
            'name': new_goods.name,
            'office_address': new_goods.office_address
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        goods = Label.objects.all()
        data = []
        for good in goods:
            data.append(
                {
                    'name': good.name,
                    'office_address': good.office_address
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)


@csrf_exempt
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_goods = Category.objects.create(**data)
        json_data = {
            'category_name': new_goods.category_name
        }
        return JsonResponse(json_data, safe=False)
    if request.method == 'GET':
        goods = Category.objects.all()
        data = []
        for good in goods:
            data.append(
                {
                    'category_name': good.category_name
                }
            )
        json_data = json.dumps(data)
        return JsonResponse(json_data, safe=False)
