from django import forms
from.models import Album

class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        # widgets = {
        #     'album_name': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Album Name',
        #         }
        #     ),
        #     'artist': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Artist',
        #         }
        #     ),
        #     'description': forms.TextInput(
        #         attrs={
        #             'placeholder': 'Description',
        #         }
        #     ),
        #     'image_url': forms.URLInput(
        #         attrs={
        #             'placeholder': 'Image URL',
        #         }
        #     ),
        #     'price': forms.NumberInput(
        #         attrs={
        #             'placeholder': 'Price'
        #         }
        #     )
        # }
        # labels = {
        #     'album_name': 'Album Name',
        #     'image_url': 'Image URL',
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()

    
    def __set_placeholders(self):
        for name, value in self.fields.items():
            placeholder = name.split('_')
            value.widget.attrs['placeholder'] = ' '.join(s.capitalize() for s in placeholder)

class AlbumCreateForm(AlbumBaseForm):
    pass

class AlbumEditForm(AlbumBaseForm):
    pass

class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()
        

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
