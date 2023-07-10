from django.conf import settings
from django.db import models
from users.models import User
from django.utils.text import slugify


class Poet(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/')
    biography = models.TextField()
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    poems = models.ManyToManyField('ClassicPoem', blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.name)
        unique_slug = original_slug
        counter = 1

        while Poet.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{counter}"
            counter += 1

        self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BasePoem(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tags', blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class ClassicPoem(BasePoem):
    author = models.ForeignKey(Poet, on_delete=models.CASCADE, null=True)


class UserPoem(BasePoem):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Tags(models.Model):
    tag = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.tag
