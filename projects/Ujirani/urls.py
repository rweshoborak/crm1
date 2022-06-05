from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('contributions.urls')),
                  path('tinymce/', include('tinymce.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
