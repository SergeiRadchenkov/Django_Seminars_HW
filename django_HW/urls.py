from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw1/', include('hw1app.urls')),
    path('hw2/', include('hw2app.urls')),
    path('hw3/', include('hw3app.urls')),
    path('hw4/', include('hw4app.urls')),
    path('hw5/', include('hw5app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
