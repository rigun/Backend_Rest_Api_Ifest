from django.contrib import admin
from .models import *

# Register your models here.
class dataKelompokAdmin (admin.ModelAdmin):
    list_display = [
        'nama_kel',
        'guru_pem',
        'asalSekolah',
        'alamatSekolah',
        'noTelpSekolah',
        'noTelpGuru',
        'noTelpKetua',
        'mailGuru',
        'mailKetua',
        'idLine',
        'username',
        'password']
    list_filter = ('username',)
    search_fields = []
    list_per_page = 25

admin.site.register(dataKelompok, dataKelompokAdmin)

class dataPesertaAdmin (admin.ModelAdmin):
    list_display = [
        'dataKel',
        'nama_leng',
        'nis',
        'foto']
    list_filter = ('nis',)
    search_fields = []
    list_per_page = 25

admin.site.register(dataPeserta, dataPesertaAdmin)
