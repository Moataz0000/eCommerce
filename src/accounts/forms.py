from django import forms
from .models import Account


class RegisterForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'country'] 


    def clean(self):
        cleaned_date = super(RegisterForm, self).clean()
        password = cleaned_date.get('password')
        confirm_password = cleaned_date.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Your Passwords don\'t match!')
        return cleaned_date
    

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email '
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['confirm_password'].widget.attrs['placeholder'] = 'Enter Confirm Password'


    