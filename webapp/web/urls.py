from rest_framework import routers
from .api import TodoViewSet, CategoryViewSet
from .views import TodoViewSet1, UserViewSet


router = routers.DefaultRouter()
router.register('api/web', TodoViewSet, 'web')
router.register('todo', TodoViewSet1, 'web')
router.register('users', UserViewSet)
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
