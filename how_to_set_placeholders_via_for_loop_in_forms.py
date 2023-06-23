from django import forms


class ModelTestForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['age']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_placeholders()
        # self.__set_disabled_fields()       #---- Disabled form fields  ----#


    def __set_placeholders(self):
        for name, value in self.fields.items():
            placeholder = name.split('_')
            value.widget.attrs['placeholder'] = ' '.join(s.capitalize() for s in placeholder)


    # Disabled form fields with for loop

    # def __set_disabled_fields(self):
    #     for field in self.fields.values():
    #         field.widget.attrs['disabled'] = 'disabled'
