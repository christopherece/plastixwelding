from django.contrib import admin
from .models import ContactInfo

# Register your models here.
from .models import GalleryImage
from .models import ServiceCategory, Service
from .models import ContactMessage



@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')
    search_fields = ('title',)
    ordering = ('-uploaded_at',)

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'facebook_url')  # Display fields in the admin panel
    search_fields = ('address', 'phone', 'email')  # Make it searchable by address, phone, and email


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)  # Filter services by category in the admin panel
    search_fields = ('name', 'description')



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'submitted_at')
    search_fields = ('full_name', 'email')
    readonly_fields = ('submitted_at',)