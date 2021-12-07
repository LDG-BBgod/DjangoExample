from django import forms
from .models import Order

class RegisterForm(forms.Form):
    quantity = forms.IntegerField(error_messages={'required': '수량을 입력해주세요'}, label='수량')
    product = forms.IntegerField(widget=forms.HiddenInput)
    
    def clean(self):
        cleaned_data = super().clean()
