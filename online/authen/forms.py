from xml.dom.minidom import Attr
from django.contrib.auth.forms import UserCreationForm
from django import forms
from authen.models import registermodel
from django.contrib.auth.hashers import make_password
class registerform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields=['username','first_name','last_name','password','age','gender','email','phone','address']
        widgets={'password':forms.PasswordInput,}
    def clean_phone(self):
        res=self.cleaned_data['phone']
        if len(str(res))!=10:
            raise forms.ValidationError('Phone number should be 10 digits')
        return res
    def clean_age(self):
        age=self.cleaned_data['age']
        if age<=15:
            raise forms.ValidationError('age should be above 15 years')
        elif age>=85:
            raise forms.ValidationError('age should be below 85 years')
        return age
    def save(self, commit=True):
        user=super(registerform,self).save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
            
            
        