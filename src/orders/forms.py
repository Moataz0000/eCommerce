from django import forms
from .models import Order, OrderPay
from django.core.exceptions import ValidationError




class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        
        
        
        
        
        
        
        
        
class OrderPayForm(forms.ModelForm):
    class Meta:
        model = OrderPay
        fields = ['pay_phone', 'pay_image']
        
    def clean_pay_phone(self):
        pay_phone = self.cleaned_data.get('pay_phone')

        if not pay_phone.isdigit():
            raise ValidationError('The phone number must contain only digits.')    

        if len(pay_phone) != 11:
            raise ValidationError('The phone number must be exactly 11 digits long.')

        valid_prefixes = ['010', '011', '012', '015']
        if not any(pay_phone.startswith(prefix) for prefix in valid_prefixes):
            raise ValidationError('The phone number must start with one of the following: 010, 011, 012, 015')


        return pay_phone    
        

