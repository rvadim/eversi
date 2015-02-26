from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return "Page: {}".format(
            self.title.encode('utf-8', errors='replace'))


class CarouselItem(models.Model):
    title = models.CharField(max_length=255)
    cut = models.TextField()
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return "CarouselItem: {}".format(
            self.title.encode('utf-8', errors='replace'))


class CircleItem(models.Model):
    title = models.CharField(max_length=255)
    cut = models.TextField()
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return "CircleItem: {}".format(
            self.title.encode('utf-8', errors='replace'))


class FeatureItem(models.Model):
    title = models.CharField(max_length=255)
    cut = models.TextField()
    image = models.ImageField()
    link = models.URLField()

    def __str__(self):
        return "FeatureItem: {}".format(
            self.title.encode('utf-8', errors='replace'))
