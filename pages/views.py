from django.shortcuts import render, redirect
from .models import GalleryImage
from .models import ContactInfo
from .models import ServiceCategory
from django.contrib import messages
from .models import ContactMessage
from .forms import ContactMessageForm

from django.core.mail import send_mail
from datetime import datetime





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
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            message = form.cleaned_data['message']
            
            form.save()  # Save to DB

            # Construct the email body with all fields
            email_body = f'''
You have a new inquiry from your website:

Name: {full_name}
Email: {email}
Phone: {phone_no}

Message:
{message}
            '''

            # Send the email using the default from address in settings
            send_mail(
                'You Have a Notification',
                email_body,
                None,  # Uses EMAIL_HOST_USER ('plastixwelding@gmail.com')
                ['hpwrepair@gmail.com', 'plastixwelding@gmail.com'],
                fail_silently=False
            )

            messages.success(request, "Your message has been submitted successfully!")
            return redirect('contact_view')
        else:
            messages.error(request, "There was an error in your submission.")
    else:
        form = ContactMessageForm()

    return render(request, 'pages/index.html', {'form': form})
