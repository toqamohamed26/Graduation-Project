from django.contrib import admin
from .models import disease,dis_symptom, dis_cause, dis_treatment, dis_diagnosis

admin.site.register(disease)
admin.site.register(dis_symptom)
admin.site.register(dis_cause)
admin.site.register(dis_treatment)
admin.site.register(dis_diagnosis)
# Register your models here.