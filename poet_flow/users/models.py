from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager
from django.utils.text import slugify


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    
    description = models.TextField()
    poems = models.ManyToManyField('home.Poem', blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = ('username', 'email', 'phone')