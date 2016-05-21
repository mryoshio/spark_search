from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

def index(req):
    items = Item.objects.order_by('release_date')
    return render(req, 'items/index.html', { 'items': items })

def detail(req, item_id):
    item = Item.objects.get(pk=item_id)
    attrs = [str(a)[str(a).rindex('.')+1:] for a in Item._meta.get_fields()]
    return render(req, 'items/detail.html', { 'item': item, 'attrs': attrs })
