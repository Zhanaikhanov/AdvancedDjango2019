from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from api.utils.constants import USER_TYPES


class MainUserManager(BaseUserManager):
    """
    Manager for MainUser
    """

    def create_user(self, username, password, user_type=None):
        """
        Method for creating user
        """
        user = self.model(username=username)
        user.set_password(password)
        user.user_type = user_type
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """
        Method for creating superuser
        """
        user = self.create_user(username, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class MainUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, blank=False, unique=True,
                                verbose_name=u"Логин", null=True)
    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False, verbose_name=u"Админ")
    user_type = models.SmallIntegerField(choices=USER_TYPES,
                                         blank=False, verbose_name=u"Тип пользователя",
                                         null=True)
    email_activated = models.BooleanField(default=False)
    image = models.CharField(max_length=2000, blank=True, null=True)

    objects = MainUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = u"Пользователь"
        verbose_name_plural = u"Пользователи"
