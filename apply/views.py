from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'riya'})

def add(request):
    
    val1=int(request.POST['fn'])
    val2=int(request.POST['sn'])
    return render(request,'output.html',{'addition':val1+val2})