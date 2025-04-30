from django.shortcuts import render, redirect
from .models import GalleryImage
from .models import ContactInfo
from .models import ServiceCategory
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactMessageForm




# Create your views here.
def index(request):
    contact = ContactInfo.objects.first()
    form = ContactMessageForm()  # Add this line

    context = {
        'contact': contact,
        'form': form
    }
    return render(request, 'pages/index.html', context)

def services(request):
    return render(request, 'pages/services.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'pages/gallery.html',{'images': images}) 

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted successfully!")
            return redirect('contact_view')
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactMessageForm()

    return render(request, 'pages/index.html', {'form':form})