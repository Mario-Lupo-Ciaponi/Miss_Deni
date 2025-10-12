from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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
            "placeholder": "Напишете потрбителско Ви име"
        })

        self.fields["email"].widget.attrs.update({
            "placeholder": "Нашете имейл адреса Ви"
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Напишете парола"
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Напишете отново паролата"
        })
