from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class CustomUserCreationForm (UserCreationForm) :

    class Meta:
        model = CustomUser
        field = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'is_writer'
        )

        # PAREI NA PARTE D_1 AOS 17 MINUTOS. 
        # PRÓXIMO PASSO IR ÀS VIEWS.