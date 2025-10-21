from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.validators import MinLengthValidator

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "username": "Потребителско име",
            "email": "Имейл адрес",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Парола"
        self.fields["password2"].label = "Потвърждаване на парола"

        self.fields["username"].widget.attrs.update({
            "placeholder": "Въведете потрбителско име"
        })

        self.fields["email"].widget.attrs.update({
            "placeholder": "Въведете имейл адреса Ви"
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Въведете парола"
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Въведете отново паролата"
        })


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Потребителско име"
        self.fields["password"].label = "Парола"

        self.fields["username"].widget.attrs.update({
            "placeholder": "Въведете потрбителско име"
        })

        self.fields["password"].widget.attrs.update({
            "placeholder": "Въведете парола"
        })


class SearchForm(forms.Form):
    query = forms.CharField(
        label="",
        max_length=150,
        validators=[
            MinLengthValidator(3),
        ],
        widget=forms.widgets.TextInput(attrs={
            "placeholder": "Потърси...",
        }),
        required=False,
    )
