from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self) -> str:
        return self.user.username


class Poet(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    poems = models.ManyToManyField('Poem', blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name


class Poem(models.Model):
    user_author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    poet_author = models.ForeignKey(Poet, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tags', blank=True)

    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Tags(models.Model):
    tag = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self) -> str:
        return self.tag