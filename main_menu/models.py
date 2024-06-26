from django.db import models


class Slogan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    video = models.URLField()

    def __str__(self):
        return self.video


class PopularProduct(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField(default=100)

    def __str__(self):
        return self.name
