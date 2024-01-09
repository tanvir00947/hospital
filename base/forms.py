from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    is_doctor = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.RadioSelect(choices=[(True, 'Doctor'), (False, 'Patient')]),
        label='Select Account Type',
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('profile_picture', 'first_name', 'last_name', 'email', 'address_line1', 'city', 'state', 'pincode', 'is_doctor')
