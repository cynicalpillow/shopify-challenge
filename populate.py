import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_challenge.settings')

import django

django.setup()

from api.models import Item

def populate():
    items = [{'name': 'apple', 'inventory': 5},
             {'name': 'banana', 'inventory': 15},
             {'name': 'pineapple', 'inventory': 25},
             {'name': 'chips', 'inventory': 7},
             {'name': 'chocolate', 'inventory': 9},
             {'name': 'china', 'inventory': 0},
             {'name': 'gpa', 'inventory': 0}]
    for dic in items:
        i = Item.objects.get_or_create(name=dic['name'])[0]
        i.inventory = dic['inventory']
        i.save()

if __name__ == '__main__':
    populate()