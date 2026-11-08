from django import forms

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "is_done"]
        widgets = {
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "tags": forms.CheckboxSelectMultiple(),
            "is_done": forms.CheckboxInput(
                attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["deadline"].input_formats = (
            ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M:%S"]
        )


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}
