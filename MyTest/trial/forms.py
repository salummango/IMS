from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import computer,Cars


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields=("username","email","password1","password2")
        
    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class Computerform(forms.ModelForm):
    class Meta:
        model=computer
        fields=('computer_name','computer_type','computer_OS','computer_HDD','computer_RAM')


class Carsform(forms.ModelForm):
    class Meta:
        model=Cars
        fields=('car_name','manufacture','engine_type','color','automation','speed','price')



