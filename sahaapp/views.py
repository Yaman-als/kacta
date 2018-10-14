from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Oyuncular, Saha_yoneticileri, Sahalar, Oyunlar, Oyuncu_tel, Oyuncu_email
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json


class SignupView(generic.CreateView):
    template_name = 'sahaapp/signup.html'
    model = Oyuncular
    fields = '__all__'


def sign_up(request):
    if request.method == "POST":
        oyuncu = Oyuncular(
            kullanici_adi=request.POST.get('kullaniciadi', ' '),
            #sifre=request.POST.get('sifre', ' '),
            adi=request.POST.get('firstname', ' '),
            soyadi=request.POST.get('lastname', ' '),
            dogum_tarihi=request.POST.get('birthdate', '2010-01-01'),
            kayit_tarihi=timezone.now(),
            aktif=False,
        )
        oyuncu.save()
        oyuncu.oyuncu_tel_set.create(tel=request.POST.get('phone', ' '))
        oyuncu.oyuncu_email_set.create(email=request.POST.get('email', ' '))
        dd = json.dumps({"welcome": "Welcome"})
        #di = {"wel": dd}
        return HttpResponse(dd, content_type='application/json')
    else:
        return render(request, 'sahaapp/signup.html')







class Login(generic.ListView):
    model = Oyuncular


# Create your views here.
