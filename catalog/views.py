from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product
from . import models
from django.views import generic
# Create your views here.


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    paginate_by = 12


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/tea-detail.html'


def index(request):
    return None