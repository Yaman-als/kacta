from django.contrib import admin
from .models import Oyuncular
from .models import Saha_yoneticileri
from .models import Sahalar
from .models import Oyunlar

admin.site.register(Oyuncular)
admin.site.register(Saha_yoneticileri)
admin.site.register(Sahalar)
admin.site.register(Oyunlar)


# Register your models here.
