from django import forms
from .models import Post


class BasePostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        widgets = {
            "title": forms.widgets.TextInput(
                attrs={
                    "placeholder": "Напиши заглавие"
                }
            ),
            "description": forms.widgets.TextInput(
                attrs={
                    "placeholder": "Напиши съдържание"
                }
            ),
        }

        labels = {
            "title": "Заглавие",
            "description": "Съдържание",
            "file": "Файл",
            "type_of_post": "Вид на пъбликацията"
        }


class AddPostModelForm(BasePostModelForm):
    ...
