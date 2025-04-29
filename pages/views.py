from django.shortcuts import render
from .models import GalleryImage

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def services(request):
    return render(request, 'pages/services.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'pages/gallery.html',{'images': images}) 