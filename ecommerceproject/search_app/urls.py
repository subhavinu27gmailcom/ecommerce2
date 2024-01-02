from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from search_app import views
app_name = "search_app"

urlpatterns = [

    path('',views.SearchResult,name='SearchResult'),

]

