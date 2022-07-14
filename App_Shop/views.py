from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from App_Shop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Product
#Get Productsall

#Serach Section Start
def search(request):
    searchword = request.GET.get('w')
    mymembers = Product.objects.filter(name__contains=searchword).values()
    template = loader.get_template('App_Shop/search.html')
    
    context = {
        'object_list': mymembers,
        'searchword':searchword,
    }
    return HttpResponse(template.render(context, request))
#Serach Section end



class  Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
