from django.forms import forms, fields, PasswordInput, ModelForm, TextInput


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] += " form-control"


class RegistrationForm(BootstrapFormMixin, forms.Form):
    email = fields.EmailField()
    password = fields.CharField(label="Пароль", widget=PasswordInput())
    password2 = fields.CharField(label="Повторите пароль", widget=PasswordInput())

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if cleaned_data["password"] != cleaned_data["password2"]:
            self.add_error(None, "Пароли не совпадают")
        return cleaned_data


class LoginForm(BootstrapFormMixin, forms.Form):
    email = fields.EmailField()
    password = fields.CharField(label="Пароль", widget=PasswordInput())
