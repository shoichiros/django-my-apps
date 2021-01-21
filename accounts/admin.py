from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from accounts.models import CustomUser


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label=False)
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=32,
        label=False,
    )
    password2 = forms.CharField(widget=forms.PasswordInput, label=False)
    privacy_check = forms.BooleanField(required=True)

    username.widget.attrs.update({'placeholder': 'Username'})
    password1.widget.attrs.update({'placeholder': 'Password(8~32文字)'})
    password2.widget.attrs.update({'placeholder': 'Password again'})

    class Meta:
        model = CustomUser
        fields = ('username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwordが一致していません。")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
