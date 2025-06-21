from django import forms
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    captcha = CaptchaField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'age', 'phone',
                  'city', 'country', 'address', 'postal_code', 'bio', 'website', 'profile_picture']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
