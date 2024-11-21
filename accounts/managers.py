from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, first_name, last_name, password, **extra_fields):
        
        if not phone:
            raise ValueError(_("The given phone number must be set"))

        user = self.model(
            phone = phone,
            first_name = first_name, 
            last_name = last_name,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, phone, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(phone=phone, first_name=first_name, last_name=last_name, password=password, **extra_fields)

    def create_superuser(self, phone, first_name, last_name, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(phone=phone, password=password, first_name=first_name, last_name=last_name, **extra_fields)