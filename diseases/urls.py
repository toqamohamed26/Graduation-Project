from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name='diseases'
urlpatterns =[
    path('<int:dis_id>',views.DiseaseDetails,name='DiseaseDetails'),

]