from django.db import models
from django import forms

# Create your models here.
class Oyuncular(models.Model):
    kullanici_adi   = models.CharField(max_length=60)
    sifre           = forms.CharField(max_length=32, widget=forms.PasswordInput)
    adi             = models.CharField(max_length=60)
    soyadi          = models.CharField(max_length=60)
    dogum_tarihi    = models.DateField()
    kayit_tarihi    = models.DateTimeField()
    aktif           = models.BooleanField()

class Oyuncu_tel(models.Model):
    oyuncu          = models.ForeignKey(Oyuncular, on_delete=models.CASCADE)
    tel             = models.CharField(max_length=20)

class Oyuncu_email(models.Model):
    oyuncu          = models.ForeignKey(Oyuncular, on_delete=models.CASCADE)
    email           = models.EmailField()

class Oyuncu_fotolari(models.Model):
    oyuncu            = models.ForeignKey(Oyuncular, on_delete=models.CASCADE)
    foto            = models.ImageField()

class Saha_yoneticileri(models.Model):
    kullanici_adi   = models.CharField(max_length=60)
    password        = forms.CharField(max_length=32, widget=forms.PasswordInput)
    adi  = models.CharField(max_length=60)
    soyadi          = models.CharField(max_length=60)
    dogum_tarihi    = models.DateField()
    kayit_tarihi    = models.DateTimeField()
    degerlendirme   = models.IntegerField()
    aktif           = models.BooleanField()

class Saha_yoneticisi_tel(models.Model):
    saha_yoneticisi = models.ForeignKey(Saha_yoneticileri, on_delete=models.CASCADE)
    tel             = models.CharField(max_length=20)

class Saha_yoneticisi_email(models.Model):
    saha_yoneticisi = models.ForeignKey(Saha_yoneticileri, on_delete=models.CASCADE)
    email           = models.EmailField()

class Odeme_sekilleri(models.Model):
    odeme_sekli     = models.CharField(max_length=40)

class Sahalar(models.Model):
    isim            = models.CharField(max_length=60)
    ucreti          = models.DecimalField(max_digits=7, decimal_places=2)
    minibus         = models.BooleanField()
    kayit_tarihi    = models.DateField()
    saha_yoneticisi = models.ForeignKey(Saha_yoneticileri, on_delete=models.CASCADE)
    odeme_sekli     = models.ForeignKey(Odeme_sekilleri, on_delete=models.CASCADE)
    degerlendirme   = models.IntegerField()

class Saha_fotolari(models.Model):
    saha            = models.ForeignKey(Sahalar, on_delete=models.CASCADE)
    foto            = models.ImageField()

class acilis_kapanis_saati(models.Model):
    pazartesi_acilis = models.TimeField()
    pazartesi_kapanis = models.TimeField()
    sali_acilis = models.TimeField()
    sali_kapanis = models.TimeField()
    carsamba_acilis = models.TimeField()
    carsamba_kapanis = models.TimeField()
    persembe_acilis = models.TimeField()
    persembe_kapanis = models.TimeField()
    cuma_acilis = models.TimeField()
    cuma_kapanis = models.TimeField()
    cumartesi_acilis= models.TimeField()
    cumartesi_kapanis = models.TimeField()
    pazar_acilis= models.TimeField()
    pazar_kapanis = models.TimeField()

class Oyunlar(models.Model):
    saha            = models.ForeignKey(Sahalar, on_delete=models.CASCADE)
    oyuncu          = models.ForeignKey(Oyuncular, on_delete=models.CASCADE)
    kayit_zamani    = models.DateTimeField()
    oyun_saati      = models.DateTimeField()
    odeme           = models.BooleanField()
