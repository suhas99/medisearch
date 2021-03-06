"""medisearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import ListView, DetailView
from medicine.models import Products ,Type

from medicine import views

urlpatterns = [

  #  url(r'^$'listView.as_view(queryset=Product.objects.all().order_by("med_name")[:15]))#,template_name="templates/base1.html"))
    
    
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
   # url(r'^admin/register/', admin.site.urls),
    url(r'^$',views.home, name='index'),
   
   
]


