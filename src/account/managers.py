from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _t


class CustomUserManager(BaseUserManager):

    def create_user(self, email:str, password:str, **other_fields):
        """ The prototype of create_user() should accept the username field, plus all required fields as arguments.
            For example, if your user model uses email as the username field, and has date_of_birth as a required field
            then create_user shuold be defined as:

            create_user(self, email, date_of_birth, password=None ...):
        """
        if not email.strip():
            raise ValueError(_t("Empty email. The email must be set."))
        
        user = self.model(
            email = self.normalize_email(email), 
            **other_fields,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email:str, password: str, **other_fields):
        """ A super user inm Django is a special type of user account that has all the permissions and privilegies 
        to manage the Django project.
        A super user can create, delete, edit and view any data or content in the project, as well as access
        the Django admin interface. Having a super user is important for setting up and maintaining the project,
        as well as troubleshooting any issue that may arise.
        """

        must_be_true_fields = ('is_staff', 'is_superuser', 'is_active')

        for field in must_be_true_fields:
            if field in other_fields and not other_fields[field]:
                raise ValueError(_t(f"Field {field} must be true or left alone."))
            other_fields[field] = True

        user = self.create_user(email, password, **other_fields)  
        user.is_admin = True  
        user.save()
        return user
