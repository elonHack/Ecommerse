from django.shortcuts import render
from item.models import Item, Category
# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories':categories, 'items':items})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')