import datetime
from django.utils import timezone
from .models import dataKelompok, dataPeserta
from rest_framework import serializers
from django.contrib.auth.models import User
from passlib.hash import pbkdf2_sha256
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
class dataKelompokSerializer(serializers.HyperlinkedModelSerializer):
    anggota = serializers.SerializerMethodField()
    
    class Meta:
        model = dataKelompok
        fields = (
            # 'url',
            'nama_kel', 
            'anggota',
            'guru_pem', 
            'asalSekolah',
            'alamatSekolah',
            'noTelpSekolah',
            'noTelpGuru',
            'noTelpKetua',
            'mailGuru',
            'mailKetua',
            'idLine',
            'pub_date',
            'username',
            'password',
            
        )
        pub_date = serializers.HiddenField(default=timezone.now())
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def create(self, validated_data):
        nama_kel    = validated_data['nama_kel'] 
        guru_pem    = validated_data['guru_pem'] 
        asalSekolah    = validated_data['asalSekolah']
        alamatSekolah    = validated_data['alamatSekolah']
        noTelpSekolah    = validated_data['noTelpSekolah']
        noTelpGuru    = validated_data['noTelpGuru']
        noTelpKetua    = validated_data['noTelpKetua']
        mailGuru    = validated_data['mailGuru']
        mailKetua    = validated_data['mailKetua']
        idLine    = validated_data['idLine']
        username    = validated_data['username']
        password    = validated_data['password']

        datakelompok_obj = dataKelompok(
            nama_kel = nama_kel, 
            guru_pem = guru_pem, 
            asalSekolah = asalSekolah,
            alamatSekolah = alamatSekolah,
            noTelpSekolah = noTelpSekolah,
            noTelpGuru = noTelpGuru,
            noTelpKetua = noTelpKetua,
            mailGuru = mailGuru,
            mailKetua = mailKetua,
            idLine = idLine,
            username = username,
            password = password
        )
        encryptPassword = pbkdf2_sha256.encrypt(validated_data['password'], rounds=12000, salt_size=32)
        datakelompok_obj.password = encryptPassword
        datakelompok_obj.save()
        return validated_data

    def get_anggota(self, obj):
        try:
            if obj.is_dataKel:
                return anggotaSerializer(obj.anggota(), many=True).data
        except:
            return None
    
class dataPesertaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = dataPeserta
        fields = (
            'dataKel',
            'nama_leng',
            'nis',
            'foto'
        )
class anggotaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = dataPeserta
        fields = (
            'nama_leng',
            'nis',
            'foto'
        )
class loginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    token = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = dataKelompok
        fields = (
            'username',
            'password',
            'token'
        )
    extra_kwargs = {'password':
                        {"write_only": True}
                    }
    def validate(self, data):
        user_obj = None
        username = data["username"]
        password = data["password"]
        if not username:
            raise serializers.ValidationError("A username is required to login.")
        user = dataKelompok.objects.filter(
               Q(username=username)
            ).distinct()
        
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username not valid")

        if user_obj:
            dataPassword = loginSerializer(user_obj)['password'].value
            if not pbkdf2_sha256.verify(password, dataPassword) :
                raise serializers.ValidationError("Incorrect credentials please try again")
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        data["token"] = token
        data["password"] = ""
        return data
