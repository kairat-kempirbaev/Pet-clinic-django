from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext

class VetUserManager(BaseUserManager):
    def create_user(self, name, password, **extra_fields):
        if not name:
            raise ValueError(gettext('Users must have a valid name'))
        user = self.model(username=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    #https://code.djangoproject.com/ticket/19067
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True, is_active=True, **kwargs)
        user.set_password(password)
        user.save()
        return user