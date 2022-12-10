from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from tensorflow import keras
import numpy as np
from keras.models import load_model
import pickle
from PIL import Image
    


def index(request):
    return render(request, 'main/index.html')


def form(request):
    return render(request, 'main/form.html')


def ref(request):
    return render(request, 'main/ref.html')


def about(request):
    return render(request, 'main/about.html')

def prescription(request):
    return render(request, 'main/prescription.html')    


def result(request):
    age = int(request.POST.get('Age'))
    hemo = request.POST.get('Hemo')
    cough = request.POST.get('coughh')
    coughing= request.POST.get('cough')
    Dyspnea = request.POST.get('Dys')
    chestpain = request.POST.get('Pain')
    withfever = request.POST.get('TH')
    Wheezing = request.POST.get('Wheezing')
    smoking = request.POST.get('smoke')
    type = request.POST.get('type')
    work = request.POST.get('work')
    dur = request.POST.get('level96')
    Triggers=request.POST.get('Triggers')
    trauma = request.POST.get('Trauma')
    fever = request.POST.get('Fever')
    weight = request.POST.get('loss')
    skin= request.POST.get('blue')
    swelling=request.POST.get('swell')
    clubbing=request.POST.get('clubbing')
    joint=request.POST.get('joint')
    
    if (cough != 1):
        cough=0
    if (fever != 1):
        fever=0
    if (Dyspnea == 0):
        exercise=1
    if(Dyspnea==1):
        shortness=1
    else:
        shortness=0
        exercise=0
    if (coughing == 1):
        prod=1
        dry=0
    elif (coughing ==0):
        prod=0
        dry=1
    else:
        prod=0
        dry=0
    if (chestpain == 1):
        sharp=1
        pleuristic=0
    elif (chestpain ==0):
        sharp=0
        pleuristic=1
    else:
        sharp=0
        pleuristic=0
    if (type == 1):
        yellow=1
        green=0
        purulent=0
    elif (type ==0):
        yellow=0
        green=1
        purulent=0
    elif (type == 2):
        yellow=0
        green=0
        purulent=1
    else:
        yellow=0
        green=0
        purulent=0
    if (withfever==0):
        sweat=1
    else :
        sweat=0
    if (withfever==1):
        malaise=1
    else :
        malaise=0
    if (withfever==2):
        chill=1
    else :
        chill=0
    if (withfever==0):
        anorexa=1
    else :
        anorexa=0
    if (Wheezing != 1):
        Wheezing=0
    if (hemo != 1):
        hemo=0
    if (skin != 1):
        skin=0
    if (Triggers != 1):
        Triggers=0
    if (age<=45):
        old=1
    else:
        old=0
    if (smoking !=1):
        smoking=0
    if (weight !=1):
        weight=0
    if (trauma !=1):
        trauma=0
    if (swelling !=1):
        swelling=0
    if (dur == 1 or dur==2):
        duration=1
    else :
        duration=0
    if (clubbing !=1):
        clubbing=0
    if (joint !=1):
        joint=0
    if (work !=1):
        work=0
    model = pickle.load(open('machine/final_model.sav', 'rb'))
    input=np.array([[cough,fever,shortness,prod,pleuristic,yellow,chill,anorexa,green,dry,Wheezing,hemo,malaise,sweat,skin,Triggers,old,smoking,weight,exercise,purulent,trauma,sharp,swelling,duration,joint,clubbing,work]])

    
    probs = model.predict_proba(input)
    predictions = model.classes_[np.argsort(probs)[:, :-3 - 1:-1]]
    probabilities = [sorted(probas, reverse=True)[:3 ] for probas in probs]
    for i in predictions:
        x=i 
    outs=list(x)
    for i in probabilities:
        x=i 
    prob=list(x)
    proba=[]
    for i in prob:
        i=int(i*100)
        proba.append(i)



    details=[]
    for i in outs:
        details.append(diseases.objects.get(Name=i))
    out=zip(details,proba)
    return render(request, 'main/result.html', {'result': out,'x':details,'pro':proba})

def machine(request):
    if request.method == "POST":
        name=request.POST.get('name')
        image=request.FILES['image']
        new=pred(img=image,name=name)
        new.save()
        path="media/"+str(pred.objects.get(name=name).img)
        #"pred/22/06/16/Tuberculosis-186.png"
        model = load_model('machine/final.h5')
        image = keras.utils.load_img(path, target_size = (224, 224)) 
        image= image.convert('L') 
        image = keras.utils.img_to_array(image)
        image = np.expand_dims(image, axis = 0)
        label = model.predict(image)
        predicted_class_indices=np.argmax(label,axis=1)
        labels = ({'COVID19': 0, 'NORMAL': 1, 'PNEUMONIA': 2, 'TURBERCULOSIS': 3})
        labels = dict((v,k) for k,v in labels.items())
        predictions = [labels[k] for k in predicted_class_indices]
        pred.objects.all().delete()
        return render(request, 'main/xray.html',{"pred":str(predictions[0]),"img":path})
    else:
        return render(request, 'main/xray.html')


    

# Create your views here.
