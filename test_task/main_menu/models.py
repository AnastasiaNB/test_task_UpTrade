from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    url = models.URLField()


class Child(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    url = models.URLField()
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name='children'
    )
