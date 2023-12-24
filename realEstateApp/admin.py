from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from .models import PropertyImage
from .models import Property
from blog.models import Blog
from user.models import User

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyImage)
admin.site.register(Blog)


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = '__all__'
        widgets = {
            'property': ForeignKeyRawIdWidget(PropertyImage._meta.get_field('property').remote_field, admin.site),
        }

class PropertyImageAdmin(admin.ModelAdmin):
    form = PropertyImageForm
