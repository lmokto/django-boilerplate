from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm


from .models import User


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User


class UserCreationForm(AuthUserCreationForm):

    error_message = AuthUserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(AuthUserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    # fieldsets = AuthUserAdmin.fieldsets + (
    #    (None, {'fields': ('webpage', 'photo')}),
    # )
