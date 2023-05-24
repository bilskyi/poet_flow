from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     description = models.TextField()
    
    
    
#     def __str__(self) -> str:
#         return self.user.username
    

class Poem(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tags')

    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.title


class Tags(models.Model):
    tag = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, db_index=True)
