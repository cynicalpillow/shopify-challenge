from django.urls import path
from api import views

urlpatterns = [
    path('item/', views.get_item, name='get_item'),
    path('list/', views.list_items, name='list_items'),
    path('purchase/', views.purchase_item, name='purchase_item')
]
