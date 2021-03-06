
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 


admin.site.site_header = "Bhat Constructions"
admin.site.site_title = "Bhat Constructions Admin Panel"
admin.site.index_title = "Welcome To Bhat Constructions Admin Panel"

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('estate.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
