from rest_framework import routers
from django.conf.urls import url
from .api import TodoViewSet, CategoryViewSet
from .views import TodoViewSet1, UserViewSet, dashboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('api/web', TodoViewSet, 'web')
router.register('todo', TodoViewSet1, 'web')
router.register('users', UserViewSet)
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = [
    url(r"^about/", dashboard, name="about"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += router.urls
