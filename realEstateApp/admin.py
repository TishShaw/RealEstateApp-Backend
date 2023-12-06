from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from .models import PropertyImage
from .models import Property

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyImage)

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = '__all__'
        widgets = {
            'property': ForeignKeyRawIdWidget(PropertyImage._meta.get_field('property').remote_field, admin.site),
        }

class PropertyImageAdmin(admin.ModelAdmin):
    form = PropertyImageForm
