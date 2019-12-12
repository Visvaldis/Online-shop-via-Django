from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Category, Product


# Create your views here.
def index(request):
    tea = Product.objects.all().order_by('?')[:6]
    return render(request,
                  "homepage/index.html",
                  context={'tea': tea})


def profile(request):
    print(User.is_authenticated)
    user = request.user
    return HttpResponse(user.get_username() + ", your profile will be soon!")
