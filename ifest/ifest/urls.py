from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from I2C import views as I2C_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i2c/', include("I2C.urls")),
    url(r'^ifoc/', include("IFOC.urls")),
    url(r'^allDataI2C/', I2C_views.data),
    # url(r'^workshop/', include("Workshop.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

