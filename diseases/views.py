from django.shortcuts import render
from . import models

def DiseaseDetails(request,dis_id):
    lis_symptoms=[]
    lis_causes=[]
    lis_treatment=[]
    lis_diagnosis=[]
    dis= models.disease.objects.get(id=dis_id)
    list_symptoms=models.dis_symptom.objects.all()
    list_causes=models.dis_cause.objects.all()
    list_treatments=models.dis_treatment.objects.all()
    list_diagnosis=models.dis_diagnosis.objects.all()
    for i in list_symptoms:
        if i.title == dis.Name:
            lis_symptoms.append(i)
    for i in list_causes:
        if i.title == dis.Name:
            lis_causes.append(i)
    for i in list_treatments:
        if i.title == dis.Name:
            lis_treatment.append(i)
    for i in list_diagnosis:
        if i.title == dis.Name:
            lis_diagnosis.append(i)
    x={'disease':dis,'symptoms':lis_symptoms,'causes':lis_causes ,'treatments':lis_treatment, 'diagnosis':lis_diagnosis}
    return render(request,'diseases/disease.html',x)
    
