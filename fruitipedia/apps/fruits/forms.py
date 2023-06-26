from django import forms
from .models import Fruit

class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for name, value in self.fields.items():
            placeholder = name.split('_')
            value.widget.attrs['placeholder'] = ' '.join(s.capitalize() for s in placeholder)

class FruitCreateForm(FruitBaseForm):
    class Meta:
        model = Fruit
        exclude=[]
        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__remove_fields_labels()

    # def __remove_fields_labels(self):
    #     for field in self.fields.values():
    #         field.label = False

class FruitEditForm(FruitBaseForm):
    pass

class FruitDeleteForm(FruitBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'