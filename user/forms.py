from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email', 'age']
        labels = {
            'fname': 'სახელი',
            'lname': 'გვარი',
            'email': 'ელ. ფოსტა',
            'age': 'ასაკი',
        }