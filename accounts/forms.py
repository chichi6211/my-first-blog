from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class ChineseUserCreationForm(UserCreationForm):
    username = forms.CharField(label='用户名', help_text='必填。只能包含字母、数字和 @/./+/-/_ 字符。')
    password1 = forms.CharField(
        label='密码',
        help_text=
        '''您的密码不能与您的其他个人信息过于相似。
    您的密码必须至少包含8个字符。
    您的密码不能是常用密码。
    您的密码不能完全为数字。'''
    )
    password2 = forms.CharField(label='确认密码', help_text='请再次输入相同的密码。')

    class Meta:
        model = User
        fields = ('username',)