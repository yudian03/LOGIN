from django import forms
from captcha.fields import CaptchaField

class Userform(forms.Form):
    username = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="密码",max_length=256,widget =forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = CaptchaField(label="验证码")

class Registerform(forms.Form):
    gender = (
        ("male", "男"),
        ("female", "女"),
    )
    username = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="确认密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="注册邮箱",widget=forms.EmailInput(attrs={'class':'form-control'}))
    sex =forms.ChoiceField(label="性别",choices=gender)
    captcha = CaptchaField(label="验证码")