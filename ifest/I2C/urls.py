from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^datakelompok/$', views.dataKelompokList.as_view(), name="list"),
    url(r'^datakelompok/login/$', views.dataKelompokLogin.as_view(), name="login"),
    url(r'^datakelompok/(?P<username>\w+)/$', views.dataKelompokDetail.as_view(), name="detail"),
    url(r'^datapeserta/$', views.dataPesertaList.as_view(), name="list"),
    url(r'^datapeserta/(?P<pk>\d+)/$', views.dataPesertaDetail.as_view(), name="detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
