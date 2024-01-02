from django.core.paginator import Paginator, InvalidPage
from django.shortcuts import render, get_object_or_404
from shopapp.models import Category, Product
def index(request):
    return render(request,'index.html',)
class Emptypage:
    pass
def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    print(1,c_slug)
    print(2,c_page)
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        print(3,c_page)
        products_list=Product.objects.all().filter(category=c_page,available=True)
        print(4,products_list)
    else:
        products_list = Product.objects.all().filter(available=True)
        print(5,products_list)
    print("c_page =",c_page)
    print("products =",products_list)
    paginator=Paginator(products_list,5)
    try:
        page=int(request.GET.get('page','1'))
        print("page",page)
    except:
        page=1
    try:
        products=paginator.page(page)
    except (Emptypage,InvalidPage):
        products=paginator.page(paginator.num_pages)
    print("output c_page,products ",c_page,products)
    return render(request,"category.html",{'category':c_page,'products':products})
def allProdDetails(request,c_slug,p_slug):
    try:
        product=Product.objects.get(slug=p_slug,category__slug=c_slug)
    except Exception as e:
        raise e
    print("c_slug, p_slug",c_slug,p_slug)
    print(product)
    return render(request,'product.html',{'products':product})