from django.db import models


class Authors(models.Model):
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class PublishingHouse(models.Model):
    namePublish = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    site = models.URLField()

    def __str__(self):
        return f'{self.namePublish}'


class Books(models.Model):
    author = models.CharField(max_length=60)
    publish = models.CharField(max_length=60)
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    yearPublish = models.DateTimeField()
    countPage = models.IntegerField()
    hardcover = models.CharField(max_length=128)
    abstract = models.CharField(max_length=128)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.title}'