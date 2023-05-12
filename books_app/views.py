from django.shortcuts import render
from rest_framework import viewsets

from books_app.models import Books, Authors, PublishingHouse
from books_app.serializers import BooksSerializer, AuthorsSerializer, PublishingHouseSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('id')
    serializer_class = BooksSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer


class PublishingHouseViewSet(viewsets.ModelViewSet):
    queryset = PublishingHouse.objects.all().order_by('id')
    serializer_class = PublishingHouseSerializer