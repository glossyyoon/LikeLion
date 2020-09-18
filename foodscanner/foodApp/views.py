from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Ingredient
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# class index(ListView):
#     template_name = 'main.html'
#     def get_queryset(self):
#         return Ingredient.objects.all

def main(request):
    template_name = 'gender.html'
    return render(request, 'gender.html')

def calculate_man(request):
    Ingredients1 = Ingredient.objects.all()
    context = {'Ingredients1':Ingredients1}
    return render(request, 'main_man.html', context)

def calculate(request):
    Ingredients1 = Ingredient.objects.all()
    context = {'Ingredients1':Ingredients1}
    return render(request, 'main.html', context)

def detail(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail.html', {"detail_key":detail_obj})

def detail_man(request, detail_id):
    detail_obj = get_object_or_404(Ingredient, pk = detail_id)
    return render(request, 'detail_man.html', {"detail_key":detail_obj})