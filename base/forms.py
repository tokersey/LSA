from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from base.models import Contact


class RegistrationForm(forms.Form):
    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label="Username",
        error_messages={'invalid': "This value must contain only letters, numbers and underscores."})
    email = forms.EmailField(
        widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label="Email address")
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label="Password")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label="Password (again)")

    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("The username already exists. Please try another one.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields did not match.")
        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        try:
            user = User.objects.get(username=self.cleaned_data['username'])
            if not check_password(self.cleaned_data['password'], user.password):
                raise forms.ValidationError('Invalid username/password combination. Please try again.')
            if not user.is_active:
                raise forms.ValidationError('This account has been disabled')
        except:
            raise forms.ValidationError('Invalid username/password combination. Please try again.')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'address', 'email', 'phone']
