from django.db import models


class Authors(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=128)
    lastName = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Publishers(models.Model):
    id = models.IntegerField(primary_key=True)
    namePublisher = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    site = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.namePublisher}'


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=60)
    publish = models.CharField(max_length=60)
    title = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    yearPublish = models.IntegerField()
    countPage = models.IntegerField()
    hardcover = models.CharField(max_length=128)
    abstract = models.CharField(max_length=128)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.title}'