from rest_framework import routers

from .views import AuthorsViewSet, BooksViewSet, PublishersViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorsViewSet)
router.register(r'books', BooksViewSet)
router.register(r'publishers', PublishersViewSet)
urlpatterns = [
    *router.urls,
]
