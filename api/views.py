from django.shortcuts import render
from django.http import JsonResponse
from api.models import Item

# Create your views here.
def get_item(request):
    if(request.method == 'GET'):
        try:
            i = Item.objects.get(pk=request.GET.get('id', ''))
            return JsonResponse({'data': [{'name': i.name, 'inventory': i.inventory}]})
        except Item.DoesNotExist:
            return JsonResponse({'error': 'no entry'}, status=400)
        except:
            return JsonResponse({'error': 'bad request'}, status=400)
    return JsonResponse({'error': 'wrong method type'}, status=400)

def list_items(request):
    if(request.method == 'GET'):
        no_inv = request.GET.get('in_stock', None)
        sort = request.GET.get('sort', 'name')
        items = []
        if(not no_inv or no_inv == 'false'):
            for i in Item.objects.order_by(sort):
                items.append({'name': i.name, 'inventory': i.inventory})
            return JsonResponse({'data': items}, status=200)
        else:
            for i in Item.objects.filter(inventory__gt=0).order_by(sort):
                items.append({'name': i.name, 'inventory': i.inventory})
            return JsonResponse({'data': items}, status=200)
    return JsonResponse({'error': 'wrong method type'}, status=400)

def purchase_item(request):
    if(request.method == 'GET'):
        try:
            i = Item.objects.get(pk=request.GET.get('id', ''))
            if(i.inventory == 0):
                return JsonResponse({'error': 'out of stock'}, status=400)
            i.inventory = i.inventory - 1
            i.save()
            return JsonResponse({'data': [{'name': i.name, 'inventory': i.inventory}]})
        except:
            return JsonResponse({'error': 'bad request'}, status=400)
    return JsonResponse({'error': 'wrong method type'}, status=400) 