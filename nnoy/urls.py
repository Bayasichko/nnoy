from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import main_page, news_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('news/', news_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)