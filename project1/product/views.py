from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView, FormView
from .models import Product
from .forms import RegisterForm
# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'

class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
    