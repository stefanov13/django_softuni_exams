from django import forms
from .models import Plant

class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        
        # widgets = {

        # }
        labels = {
            'image_url': 'Image URL',
            
        }

class PlantCreateForm(PlantBaseForm):
    pass