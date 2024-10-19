import debug_toolbar.urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('store.urls', namespace='store')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls',namespace='cart')),
    path('oreders/', include('orders.urls', namespace='orders')),
    
    
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)