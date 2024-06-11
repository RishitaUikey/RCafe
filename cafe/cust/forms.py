from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email= forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    first_name=forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name=forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}))
    
    class Meta:
        model = User
        fields= ['username', 'first_name','last_name','email','password1','password2']
        
    def __init__(self, *args, **kwargs) :
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='UserName'
    
        
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        
        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Conform Password'

