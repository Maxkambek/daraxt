from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise TypeError('Email not')
        user = self.model(phone=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if not password:
            raise TypeError('password no')
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    ROLE = (
        (1, 'Daraxt ektiruvchi'),
        (2, 'Daraxt ekuvchi')
    )
    username = models.CharField(max_length=50, unique=True, db_index=True)
    image = models.ImageField(null=True, blank=True, upload_to='accounts/')
    phone = models.CharField(max_length=14, null=True, blank=True)
    role = models.IntegerField(choices=ROLE, default=1)
    bio = models.TextField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_login = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = _("Telefon raqamni tasdiqlash")
        verbose_name_plural = _("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name=_("Phone number"))
    code = models.CharField(max_length=10, verbose_name=_("Code"))

    def __str__(self):
        return self.phone
