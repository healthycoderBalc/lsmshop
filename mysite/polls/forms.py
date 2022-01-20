from msilib.schema import CheckBox
from django import forms
from .models import *
import ipywidgets as Nwidgets

# create a ModelForm
class ClientForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Client
        fields = "__all__"
        widgets = {
            'fechaNacimiento': forms.SelectDateWidget
        }

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
            'formasContacto': forms.CheckboxSelectMultiple
        }

class BusinesshourdayForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Businesshourday
        fields = "__all__"

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