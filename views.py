from django.shortcuts import render
from .models import StockItem
# Create your views here.
def login_page(request):
    return render(request,'login.html')
def dashboard(request):
    items = StockItem.objects.all()
    return render(request,'dashboard.html',{'items':items})
def add_stock(request):
    return render(request,'add_stock.html')
def reports(request):
    return render(request,'reports.html')
def stock(request):
    return render(request,'stock.html')
