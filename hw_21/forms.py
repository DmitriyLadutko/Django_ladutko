from django.forms import ModelForm

from hw_21.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
