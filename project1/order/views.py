from re import template
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm
from django.utils.decorators import method_decorator
from fcuser.decorators import login_required
from django.views.generic import ListView
from .models import Order

# Create your views here.

class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str)


    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw

@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset