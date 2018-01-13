from django.shortcuts import get_object_or_404, render
from django.contrib.auth import views
from django.contrib.auth.models import User

from .models import dataKelompok, dataPeserta
from .serializers import dataKelompokSerializer, dataPesertaSerializer, loginSerializer
from .paginations import dataPageNumberPagination

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


######################################################################
def data(request):
    dataK = None
    dataP = None
    dataK = dataKelompok.objects.all()
    dataP = dataPeserta.objects.all()
    return render(request, 'postlist.html', {'dataK':dataK, 'dataP':dataP})

######################################################################
class dataKelompokList(generics.ListCreateAPIView):
    pagination_class = dataPageNumberPagination
    queryset = dataKelompok.objects.all()
    serializer_class = dataKelompokSerializer

class dataKelompokLogin(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = loginSerializer
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = loginSerializer(data = data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status= HTTP_200_OK)
        return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)

class dataKelompokDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = dataKelompok.objects.all()
    serializer_class = dataKelompokSerializer
    lookup_field = 'username'

class dataPesertaList(generics.ListCreateAPIView):
    pagination_class = dataPageNumberPagination
    queryset = dataPeserta.objects.all()
    serializer_class = dataPesertaSerializer


class dataPesertaDetail(generics.RetrieveUpdateDestroyAPIView):
    pagination_class = dataPageNumberPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAuthenticated)
    queryset = dataPeserta.objects.all()
    serializer_class = dataPesertaSerializer


