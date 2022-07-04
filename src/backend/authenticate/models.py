from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self, email: str, password = str, first_name: str = None, last_name: str = None, phone: str = None, customer: str = None, department: str = None):
        
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=self.user,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            customer=customer,
            department=department,
        )

        # Create and save user to DDBB
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str):
        """
        Creates and saves a superuser with the given credentials.

        :param email: str - The email address of the user.
        :param password: str - The password of the user.
        """

        user = self.model(
            email=self.normalize_email(email),
            username=self.user,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            customer=customer,
            department=department,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(AbstractBaseUser):
    """
    User model
    """
    email = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    username= models.CharField(max_length=30,unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    customer = models.CharField(max_length=90, blank=True, null=True)
    department = models.CharField(max_length=90, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AccountManager()

    class Meta:
        db_table = "users_table"

    def __str__(self):
        return str(self.email)


    def has_perm(self, perm, obj=None): 
        return self.is_active

    def has_module_perms(self, app_label): 
        return self.is_superuser