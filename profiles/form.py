from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from.models import Roles, Permission


class LogInForm(forms.Form):
    username = forms.CharField(label="Username:", min_length=4, max_length=25)
    password = forms.CharField(label="Password:", min_length=8, widget=forms.PasswordInput)


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Username:', min_length=4, max_length=25, validators=[
        RegexValidator(regex=r'^[0-9A-Za-z-_.]+$', message="Invalid type")],
                               help_text="Username can consist words, digits and symbols ./-/_")
    email = forms.EmailField(label="Email:", help_text="my_email@example.com")
    role_name = forms.ChoiceField(label="Role:", widget=forms.Select, choices=[('Administrator', 'Administrators'),
                                                                               ('Editor', 'Editors'),
                                                                               ('User', 'Users')])
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput, strip=False,
                                help_text=["Password shouldn't be too simple.",
                                           "Password must be at least 8 symbols.",
                                           "Password can't be digits only"])
    password2 = forms.CharField(label="Confirm Password:", widget=forms.PasswordInput, strip=False,
                                help_text="Re-enter password.")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError(_("This username already exists."), code='invalid')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError(_("This email is already in use."), code='invalid')
        return email

    def clean_role_name(self):
        role_name = self.cleaned_data['role_name']

        if role_name in ['Administrator', 'Editor']:
            Roles.objects.get_or_create(name=role_name, premoderation=False)
        else:
            Roles.objects.get_or_create(name=role_name, premoderation=True)
        return role_name

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 is not None and validate_password(password1) is None:
            if password1 and password2 and password1 != password2:
                raise ValidationError(_("Passwords don't much."), code='invalid')
        else:
            ValidationError(_(""), code='invalid')
        return password2

    def save(self, commit=True):
        role_name = self.cleaned_data['role_name']
        role = Roles.objects.get(name=role_name)
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        Permission.objects.create(user=user, role=role)
        return user
