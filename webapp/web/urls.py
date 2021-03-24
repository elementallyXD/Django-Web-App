from rest_framework import routers
from django.conf.urls import url
from django.urls import include, path
from .api import TodoViewSet, CategoryViewSet
from .views import TodoViewSet1, UserViewSet, dashboard
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('api/web', TodoViewSet, 'web')
router.register('todo', TodoViewSet1, 'web')
router.register('users', UserViewSet)
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = [
    url(r"^about/", dashboard, name="about"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += router.urls
