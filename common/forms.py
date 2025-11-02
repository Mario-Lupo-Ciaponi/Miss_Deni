from django import forms
from django.core.validators import MinLengthValidator

from .mixins import MakeAllFieldsRequiredMixin



class ContactForm(MakeAllFieldsRequiredMixin, forms.Form):
    REASON_CHOICES = [
        ('courses', 'Интерес към часовете'),
        ('prices', 'Запитване за цени'),
        ('organization', 'Организационни въпроси'),
        ('feedback', 'Обратна връзка или други запитвания'),
    ]

    first_name = forms.CharField(
        max_length=100,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "напр. Дени"
            }
        ),
        label="Собствено име",
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "напр. Стефанова"
            }
        ),
        label="Фамилно име",
    )
    email = forms.EmailField(
        label="Имейл адрес",
    )
    phone_number = forms.IntegerField(
        label="Телефонен номер",
    )
    select_subject = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=REASON_CHOICES,
        label="Причина за писане",
    )
    message = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Напишете Вашето съобщение...",
            }
        ),
        label="Съобщение",
    )

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
