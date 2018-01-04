import datetime
from django.db import models
from django.utils import timezone
from passlib.hash import pbkdf2_sha256

class dataKelompok(models.Model):
    nama_kel = models.CharField(max_length=60, blank=True)
    guru_pem = models.CharField(max_length=60)
    asalSekolah = models.CharField(max_length=60)
    alamatSekolah = models.CharField(max_length=200)
    noTelpSekolah = models.CharField(max_length=14)
    noTelpGuru = models.CharField(max_length=14)
    noTelpKetua = models.CharField(max_length=14)
    mailGuru = models.CharField(max_length=100)
    mailKetua = models.CharField(max_length=100)
    idLine = models.CharField(max_length=40)
    password = models.CharField(max_length=256)
    username = models.CharField(max_length=100, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nama_kel
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def anggota(self):
        try:
            return dataPeserta.objects.filter(dataKel=self)
        except:
            return None
    def is_dataKel(self):
        if dataPeserta.dataKel is None:
            return False
        return True

class dataPeserta(models.Model):
    dataKel = models.ForeignKey(dataKelompok, on_delete=models.CASCADE)
    nama_leng = models.CharField(max_length=60)
    nis = models.IntegerField(default=0)
    def __str__(self):
        return self.nama_leng
    