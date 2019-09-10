from django import forms
from .models import User
from .choices import USER_TYPES


class UserAdminForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        choices=USER_TYPES,
        label="User Type",
        initial='',
        widget=forms.Select(),
        required=False
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type',
        )
