from django import forms
from book.models import Allbooks


class AllbooksModelForm(forms.ModelForm):
    class Meta:
        model = Allbooks
        fields = '__all__'


    def clean_name(self):
        name = self.cleaned_data['name']
        if Allbooks.objects.filter(name=name).exists():
            raise forms.ValidationError("This name already exists")
        return name
