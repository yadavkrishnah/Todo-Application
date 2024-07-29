from django import forms
from django.contrib.auth.models import User
from.models import Todos

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"First_name"}),
            "last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"last_name"}),
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"usernmae"}),
            "email":forms.TextInput(attrs={"class":"form-control","placeholder":"Email"}),
            "password":forms.TextInput(attrs={"class":"form-control","placeholder":"password"})



        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"usernmae"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}),
}


class TodoForms(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['title','content']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"content"}),
        }


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=['title','content','status']
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"title"}),
            "content":forms.TextInput(attrs={"class":"form-control","placeholder":"content"}),
            "status":forms.CheckboxInput(attrs={"class":"form-check-input","placeholder":"status"}),

        }