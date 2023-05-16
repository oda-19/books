from .models import Authors, Books, Publishers
from rest_framework import serializers


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = '__all__'
