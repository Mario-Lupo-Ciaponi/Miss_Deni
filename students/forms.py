from django import forms

from .models import Group, Student


class BaseGroupModelForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.filter(group__isnull=True),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Добави ученици към групата:"
    )

    class Meta:
        model = Group
        fields = ["name", "students"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            qs = Student.objects.filter(group__isnull=True) | Student.objects.all()
            self.fields["students"].queryset = qs.distinct()
            self.fields["students"].initial = self.instance.students.all()
        else:
            self.fields["students"].queryset = Student.objects.filter(group__isnull=True)

    def save(self, commit=True):
        group = super().save(commit=False)

        if group:
            group.save()
            selected = self.cleaned_data.get("students") or Student.objects.none()

            selected_ids = list(selected.values_list("pk", flat=True))

            Student.objects.filter(group=group).exclude(pk__in=selected_ids).update(group=None)
            Student.objects.filter(pk__in=selected_ids).update(group=group)

        return group


class CreateGroupModelForm(BaseGroupModelForm):
    ...


class UpdateGroupModelForm(BaseGroupModelForm):
    ...
