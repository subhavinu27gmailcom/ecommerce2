
from django.urls import path

from shopapp import views
app_name = 'shopapp'

urlpatterns = [

    path('',views.allProdCat,name='allProdCat'),

    path("<slug:c_slug>/",views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>',views.allProdDetails,name='products_by_details'),



]