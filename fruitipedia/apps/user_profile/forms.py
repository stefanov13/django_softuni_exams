from django import forms
from .models import Profile

class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    def __set_placeholders(self):
        for name, value in self.fields.items():
            placeholder = name.split('_')
            value.widget.attrs['placeholder'] = ' '.join(s.capitalize() for s in placeholder)

class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['image_url', 'age']
        widgets = {
            'password': forms.TextInput(
                attrs={'type': 'password'}
            )
        }
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': '',
        }

class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['email', 'password', ]
