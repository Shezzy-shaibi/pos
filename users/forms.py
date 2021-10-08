from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import CustomUser

from allauth.account.forms import LoginForm, SignupForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', }))
    country = forms.CharField(label='country', widget=forms.TextInput(attrs={'class': 'form-control', }))
    city = forms.CharField(label='city', widget=forms.TextInput(attrs={'class': 'form-control', }))

    zip_code = forms.CharField(label='ZipCode', widget=forms.TextInput(attrs={'class': 'form-control', }))
    address1 = forms.CharField(label='Address1', widget=forms.TextInput(attrs={'class': 'form-control', }))
    address2 = forms.CharField(label='Address2', widget=forms.TextInput(attrs={'class': 'form-control', }))
    # phone_regex = RegexValidator(regex=r"^\+(?:[0-9]*?){6,14}[0-9]$",
    #                              message=_("Enter a valid international mobile number"))
    mobile_phone = forms.CharField(label = "Mobile phone", max_length=99 )
    # additional_information = forms.CharField(label = "Additional information", max_length=1024
    #                                        )


    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name' ,'address1','address2','zip_code','city','country','mobile_phone')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','first_name','last_name' ,'address1','address2','zip_code','city','country','mobile_phone')


class UserDetailChangeForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly' }))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter first name' }))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter last name' }))

    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter city name' }))
    # country = forms.CharField(label='country', widget=forms.TextInput(attrs={'class': 'form-control', }))
    # country = CountryField(blank_label='select country' ).formfield(label='Country\n', widget=forms.Select(attrs={'class': 'form-control bg-secondary text-white'}))
    country = CountryField(blank_label='select country' ).formfield( widget=forms.Select(attrs={'style':' border: 3px solid whitesmoke;height:48px; width: 100%;padding: 10px;margin: -5px; margin-left: -0px;font-size: 16px;' }))
    # country = forms.CharField(label='Country',required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter country name' }))
    state = forms.CharField(label='State',required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter state name','value':'None' }))
    zip_code = forms.CharField(label='Zip Code', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter zip code' }))
    address1 = forms.CharField(label='Address1', widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter address line1' }))
    address2 = forms.CharField(label='Address2', required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter address line2', 'value':'None' }))
    mobile_phone = forms.CharField( label='Mobile phone',  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter mobile number'}))
    # additional_information = forms.CharField(required=False,label='Additional information', widget=forms.TextInput(attrs={'class': 'form-control', 'required':'' }))


    class Meta:
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','address1','address2','zip_code','city','country','state','mobile_phone']
        widgets = {'country': CountrySelectWidget()}
