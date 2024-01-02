from django.db.models import Q
from django.shortcuts import render

from shopapp.models import Product


# return render(request,'search_app.html')


#def search_app(request):
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(descriptions__contains=query))
        print(type(query),type(products))
        return render(request,'search.html',{'query':query,'products':products})