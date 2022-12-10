from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [path('', views.index, name='index'),
                path('form', views.form, name='form'),
                path('ref', views.ref, name='ref'),
                path('about', views.about, name='about'),
                path('result', views.result, name='result'),
                path('machine', views.machine, name='machine'),
                path('prescription', views.prescription, name='prescription'),
]
