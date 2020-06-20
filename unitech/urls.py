from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from .configs.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('unitech.apps.base.urls')),
    url(r'^login/', include('unitech.apps.login.urls')),
    url(r'^cadastro/', include('unitech.apps.cadastro.urls')),
]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
