from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/haker/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
    path('pdf/', include('pdf.urls')),
    path('amaliyot/', include('amaliyot.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
