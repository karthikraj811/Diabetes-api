from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pickle
import pandas as pd


def home(request):
    return render(request,'home.html')

def result(request):
    print(request)
    if request.method== 'POST':
        Age = float(request.POST['age'])
        print(type(Age))
        Gender	= 1 if request.POST['gender']=='Male' or request.POST['gender']=='male'  else 0

        Polyuria = 1 if request.POST['polyuria']=='yes' or request.POST['polyuria']=='Yes' or request.POST['polyuria']=='YES' else 0

        Polydipsia = 1 if request.POST['polydipsia']=='yes' or request.POST['polydipsia']== 'Yes' or request.POST['polydipsia']=='YES' else 0

        sudden_weight_loss = 1 if request.POST['sudden_weight']=='yes' or request.POST['sudden_weight']=='Yes' or request.POST['sudden_weight']=='YES' else 0

        
        weakness	= 1 if request.POST['weakness']=='yes' or request.POST['weakness']=='Yes' or request.POST['weakness']=='YES' else 0

        Polyphagia	= 1 if request.POST['polyphagia']=='yes' or request.POST['polyphagia']=='Yes' or request.POST['polyphagia']=='YES' else 0

        Genital_thrush	= 1 if request.POST['genital']=='yes' or request.POST['genital']=='Yes' or request.POST['genital']=='YES' else 0

        visual_blurring	= 1 if request.POST['visual_blur']=='yes' or request.POST['visual_blur']== 'Yes' or request.POST['visual_blur']== 'YES'  else 0

        Itching= 1 if request.POST['itch']=='yes' or request.POST['itch']=='Yes' or request.POST['itch']=='YES' else 0

        Irritability = 1 if request.POST['irrit']=='yes' or request.POST['irrit']=='Yes' or request.POST['irrit']=='YES' else 0

        delayed_healing	= 1 if request.POST['delayed_heal']=='yes' or request.POST['delayed_heal']=='Yes' or request.POST['delayed_heal']=='YES' else 0

        partial_paresis	= 1 if request.POST['paresis']=='yes' or request.POST['paresis']=='Yes' or request.POST['paresis']=='YES' else 0

        muscle_stiffness = 1 if request.POST['muscle_stiff']=='yes' or request.POST['muscle_stiff']== 'Yes' or request.POST['muscle_stiff']== 'YES' else 0

        Alopecia	= 1 if request.POST['alopecia']=='yes' or request.POST['alopecia']=='Yes' or request.POST['alopecia']=='YES' else 0

        Obesity	= 1 if request.POST['obesity']=='yes' or request.POST['obesity']=='Yes' or request.POST['obesity']=='YES' else 0

        input_ = pd.DataFrame([[Age, Gender, Polyuria, Polydipsia, sudden_weight_loss,weakness, Polyphagia, Genital_thrush, visual_blurring,Itching, Irritability, delayed_healing, partial_paresis,muscle_stiffness, Alopecia, Obesity]])

        model = pickle.load(open('diabetes.pkl','rb'))

        result = model.predict(input_)[0]

       
        if result==1:

            return render(request,'home.html',{'result':'Postive'})
        else:
            return render(request,'home.html',{'result':'Negative'})

