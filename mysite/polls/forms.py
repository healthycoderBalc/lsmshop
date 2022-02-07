from curses.panel import bottom_panel
from msilib.schema import CheckBox
from attr import attr, attrs
from django import forms
from .models import *
import ipywidgets as Nwidgets
from bootstrap_datepicker_plus.widgets import TimePickerInput
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms import bootstrap


# create a ModelForm
class ClientForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Client
        fields = "__all__"
        exclude = ['privilegios']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(username = self.user)
        # print(self.fields['user'].queryset)

class SubscriptionForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Subscription
        fields = "__all__"

class DayweekForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Dayweek
        fields = "__all__"

class HeadingForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Heading
        fields = "__all__"

class ContactFormForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = ContactForm
        fields = "__all__"


class BusinessForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Business
        fields = "__all__"
        widgets = {
            'rubros': forms.CheckboxSelectMultiple,
            'formasContacto': forms.CheckboxSelectMultiple,
            'diasSemana': forms.CheckboxSelectMultiple
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BusinessForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Client.objects.filter(user = self.user)
        print(self.fields['cliente'].queryset)



class BusinesshourdayForm(forms.ModelForm):
    # specify the name of model to use

    class Meta:
        model = Businesshourday
        fields = "__all__"
        widgets = {
            'horaAbre': TimePickerInput(),
            'horaCierra': TimePickerInput(),
            # 'negocio': forms.Select(attrs={"disabled" : "disabled"})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["negocio"].disabled = True
        self.fields["diaSemana"].disabled = True

class BusinessAreaForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = BusinessArea
        fields = "__all__"

class BusinessContactFormForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = BusinessContactForm
        fields = "__all__"
        widgets = {
            'datosContacto': forms.TextInput(attrs={'placeholder': 'para Nº incluir el 15, ej: 343154444444'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["formaContacto"].disabled = True
        self.fields["negocio"].disabled = True

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)



class DateRangeForm(forms.Form):
    dia = forms.ModelChoiceField(queryset = Dayweek.objects.all())
    start_date = forms.TimeField(required=True, widget=TimePickerInput())
    end_date = forms.TimeField(required=True, widget=TimePickerInput())