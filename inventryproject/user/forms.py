from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation


class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old password"),strip=False,widget=forms.PasswordInput(attrs={"class":"form-control","autocomplete":"current-password","autofocus":True}))
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={"class":"form-control"
    ,"autocomplete":"new-password"}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control"}))

class MyPasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email',
                                                                                            'class':'form-control'}))
class MySetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={"class":"form-control"
    ,"autocomplete":"new-password"}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control"}))

class CreateUserForm(UserCreationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class UserUpdateForm(forms.ModelForm):
    username =forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=['username','email']
    
class ProfileUpdateForm(forms.ModelForm):
    address=forms.CharField(widget=forms.TimeInput(attrs={'autofocus':True,'class':' form-control addr','id':'addr'}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={'autofocus':True,'class':'form-control'}))
    class Meta:
        model=Profile
        fields=['address','phone','image']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput
                               (attrs={'autocomplete':'current-password','class':'form-control'}))