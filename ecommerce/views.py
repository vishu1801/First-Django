from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    prods = Products.objects.all()
    return render(request,"index.html",{'prods': prods})