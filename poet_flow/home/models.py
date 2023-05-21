from django.db import models

class Poem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    #author = models.ForeignKey()
    #tags