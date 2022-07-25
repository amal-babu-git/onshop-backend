from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from storefront.settings.dev import MEDIA_ROOT


# Customize Admin Interface
admin.site.site_header = "OnShop Admin"
admin.site.index_title = "Admin"

# URLs
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    #jwt
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # jwt customized auth with this TODO:experimental
    path('core/',include('core.urls')),
    path('store/', include('store.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)

    urlpatterns += [path('silk/', include('silk.urls', namespace='silk')),
                    path('__debug__/', include(debug_toolbar.urls))]
