from django import forms
from django.forms.widgets import PasswordInput
from .models import Fcuser
from django.contrib.auth.hashers import check_password, make_password

class RegisterForm(forms.Form):
    email = forms.EmailField(error_messages={'required': '이메일을 입력해주세요'}, max_length=64, label='이메일')
    password = forms.CharField(error_messages={'required': '비밀번호를 입력해주세요'}, widget=forms.PasswordInput, label='비밀번호')
    repassword = forms.CharField(error_messages={'required': '비밀번호를 입력해주세요'}, widget=forms.PasswordInput, label='비밀번호 확인')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')

        if password and repassword:
            if password != repassword:
                self.add_error('repassword', '비밀번호가 다릅니다.')
            else:
                fcuser = Fcuser(
                    email=email,
                    password=make_password(password)
                )
                fcuser.save()

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'required': '이메일을 입력해주세요'}, max_length=64, label='이메일')
    password = forms.CharField(error_messages={'required': '비밀번호를 입력해주세요'}, widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                fcuser = Fcuser.objects.get(email=email)
            except Fcuser.DoesNotExist:
                self.add_error('email', '아이디가 없습니다')
                return
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다')
            else:
                self.email = fcuser.email


