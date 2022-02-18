# from asyncio.streams import _ClientConnectedCallback
# from curses.panel import bottom_panel
from msilib.schema import CheckBox
# from sys import last_traceback
from attr import attr, attrs
from django import forms
from .models import *
import ipywidgets as Nwidgets
from bootstrap_datepicker_plus.widgets import TimePickerInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms import bootstrap
from django.forms.models import fields_for_model



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
        self.fields["paid"].disabled = True
        self.fields["fecha_ultimo_pago"].disabled = True



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

helpText = "La contraseña no puede ser muy similar a los otros datos; debe contener al menos 8 caracteres; no puede ser muy común; no puede contener solo números<br><br>"

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=64)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
    
    def __init__(self, *args, **kwargs):
        super(RegistroForm, self).__init__(*args, **kwargs)

        self.fields['password1'].help_text = helpText
        self.fields['username'].help_text = "150 caracteres o menos. Solamente letras, digitos y @/./+/-/_ <br><br>"
        self.fields['first_name'].help_text = "<br>"
        self.fields['last_name'].help_text = "<br>"
        self.fields['email'].help_text = "Ingrese una dirección válida <br><br>"
        self.fields['password2'].help_text = "Ingrese la misma contraseña, para verificación <br><br>"
        
        self.fields['password1'].label = "Contraseña"
        self.fields['username'].label = "Usuario"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellido"
        self.fields['password2'].label = "Confirme la contraseña"


class AutenticacionForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(AutenticacionForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = "Contraseña"
        self.fields['username'].label = "Usuario"



class DateRangeForm(forms.Form):
    dia = forms.ModelChoiceField(queryset = Dayweek.objects.all())
    start_date = forms.TimeField(required=True, widget=TimePickerInput())
    end_date = forms.TimeField(required=True, widget=TimePickerInput())

class PerfilForm(forms.ModelForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address')

# class PerfilcitoForm(ClientForm):
#     first_name = User._meta.get_field('first_name').formfield()
#     last_name = User._meta.get_field('last_name').formfield()
#     email = User._meta.get_field('email').formfield()

#     class Meta(ClientForm.Meta):
#         model = Client
#         fields = ClientForm.Meta.fields + ['first_name', 'last_name', 'email']

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)
#         super(PerfilcitoForm, self).__init__(*args, **kwargs)
#         self.fields['user'].queryset = User.objects.filter(username = self.user)
#         # print(self.fields['cliente'].queryset)

class profileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

