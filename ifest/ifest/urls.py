from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from I2C import views as I2C_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i2c/', include("I2C.urls")),
    url(r'^ifoc/', include("IFOC.urls")),
    url(r'^allDataI2C/', I2C_views.data),
    # url(r'^workshop/', include("Workshop.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]