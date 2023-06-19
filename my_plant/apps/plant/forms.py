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

class PlantEditForm(PlantBaseForm):
    pass

class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    # def save(self, commit=True):
    #     if self.instance:
    #         self.instance.delete()
    #     return self.instance

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
