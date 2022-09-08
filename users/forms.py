from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


# I'll use built in validations, hash creation etc, but won't render it
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Do I need first_name here? I deleted it here,
        # just for future reference
        fields = ("username", "email")

    def save(self, commit=True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
