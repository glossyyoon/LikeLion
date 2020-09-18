from django.shortcuts import render
from .models import Orders, Members, Sheets

# Create your views here.
def index(request):
    order_rows = Orders.objects.all()
    truck = Sheets.objects.all()

    return render(request, 'home.html', {'order_rows':order_rows, 'truck':truck})