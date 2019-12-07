from django.shortcuts import render
from catalog.models import Category, Product
from random import shuffle
# Create your views here.
def index(request):
    tea = Product.objects.all().order_by('?')[:6]
    return render(request,
                  "homepage/index.html",
                  context={'tea': tea})