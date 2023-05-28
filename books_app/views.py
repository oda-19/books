from rest_framework import viewsets

from books_app.models import Books, Authors, Publishers
from books_app.serializers import BooksSerializer, AuthorsSerializer, PublishersSerializer
from rest_framework.permissions import IsAuthenticated

import logging

logger = logging.getLogger(__name__)


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('id')
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer
    permission_classes = [IsAuthenticated]


class PublishersViewSet(viewsets.ModelViewSet):
    queryset = Publishers.objects.all().order_by('id')
    serializer_class = PublishersSerializer
    permission_classes = [IsAuthenticated]
