from django.urls import path
from . import views

app_name = 'sahaapp'

urlpatterns = [
    path('signup/', views.sign_up, name='olustur'),
]

#    path('signup/', views.SignupView.as_view(), name='signup'),