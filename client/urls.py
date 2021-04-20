from django.contrib import admin
from django.urls import path
from .views import SignUpView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('admin/', admin.site.urls),
    #path('', include('service.urls', namespace='service')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
