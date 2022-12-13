
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter


from store.views import BookViewSet, auth

router = SimpleRouter()

router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
]

urlpatterns += router.urls
