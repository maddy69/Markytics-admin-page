
from django.contrib import admin
from django.urls import include , path
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name ='index'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
