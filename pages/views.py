from django.shortcuts import render
from .models import GalleryImage
from .models import ContactInfo
from .models import ServiceCategory


# Create your views here.
def index(request):
    contact = ContactInfo.objects.first()
    context = {
        'contact': contact
    }
    return render(request, 'pages/index.html', context)

def services(request):
    return render(request, 'pages/services.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'pages/gallery.html',{'images': images}) 