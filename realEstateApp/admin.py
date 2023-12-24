from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from .models import PropertyImage
from .models import Property
from blog.models import Blog
from user.models import User

# Register your models here.

admin.site.register(PropertyImage)
admin.site.register(Blog)

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'price')  # Ensure 'id' is not here
    ordering = ('slug',)  # Use 'slug' or other fields for ordering
    # ... any other configurations ...
admin.site.register(Property, PropertyAdmin)

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = '__all__'
        widgets = {
            'property': ForeignKeyRawIdWidget(PropertyImage._meta.get_field('property').remote_field, admin.site),
        }

class PropertyImageAdmin(admin.ModelAdmin):
    form = PropertyImageForm
