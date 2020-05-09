"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django_test import views
from django.conf.urls.static import static
from rest_framework import routers
from articles.api_views import TagViewSet, ArticleViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('tag', TagViewSet)
router.register('article', ArticleViewSet)

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('users/', include('users.urls')),
    path('api/v0/', include(router.urls))
]

# module x.x.x (numpy 12.1.2)

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
