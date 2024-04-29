from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserSignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']