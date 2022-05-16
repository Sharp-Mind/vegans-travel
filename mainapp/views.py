from django.shortcuts import render
from django.conf import settings
from mainapp.models import Posts


def main(request):
  
    context = {
        'posts': Posts.objects.all(),
        "media_url": settings.MEDIA_URL
    }
    
    return render(request, "mainapp/index.html", context)


def products(request):
    return render(request, "mainapp/products.html")


def contact(request):
    return render(request, "mainapp/contact.html")