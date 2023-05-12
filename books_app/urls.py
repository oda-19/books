from rest_framework import routers

from .views import AuthorsViewSet, BooksViewSet, PublishingHouseViewSet


router = routers.DefaultRouter(trailing_slash=True)
router.register(r'authors', AuthorsViewSet, basename='newssite')
router.register(r'books', BooksViewSet, basename='newstags')
router.register(r'PublishingHouses', PublishingHouseViewSet, basename='userssite')
urlpatterns = [
    *router.urls,
]
