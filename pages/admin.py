from django.contrib import admin

# Register your models here.
from .models import GalleryImage

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')
    search_fields = ('title',)
    ordering = ('-uploaded_at',)
