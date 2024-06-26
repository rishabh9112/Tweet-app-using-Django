from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TweetForm(forms.ModelForm): 
    class Meta:
        model = Tweet
        fields =['text', 'photo'] 
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    
    
    
class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
