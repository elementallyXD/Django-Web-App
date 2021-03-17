from rest_framework import routers
from .api import TodoViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register('api/web', TodoViewSet, 'web')
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
