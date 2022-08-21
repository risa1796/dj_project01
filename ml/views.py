#from fcntl import DN_DELETE
from django.shortcuts import render
import joblib
import pandas as pd
import pickle

def inputdata(request):
    return render(request,'ml/inputdata.html')

def ml_result(request):
    cls = joblib.load('ml/tcl_model.pkl')

    df = pd.DataFrame(columns=['family', 'pclass_1', 'pclass_2', 'pclass_3', 'sex_female', 'sex_male',
       'embarked_C', 'embarked_Q', 'embarked_S', 'age_Adult', 'age_Baby',
       'age_Child', 'age_Elderly', 'age_YoungAdult', 'age_Teenager',
       'title_Master', 'title_Miss', 'title_Mr', 'title_Mrs', 'title_Other'])

    lis = []
    lis.append(request.GET['family'])

    if request.GET['pclass'] == 'Class 1':
        lis.extend([1,0,0])
    elif request.GET['pclass'] == 'Class 2':
        lis.extend([0,1,0])
    elif request.GET['pclass'] == 'Class 3':
        lis.extend([0,0,1])

    if request.GET['gender'] == 'Female':
        lis.extend([1,0])
    elif request.GET['gender'] == 'Male':
        lis.extend([0,1])

    if request.GET['embarked'] == 'Embarked C':
        lis.extend([1,0,0])
    elif request.GET['embarked'] == 'Embarked Q':
        lis.extend([0,1,0])
    elif request.GET['embarked'] == 'Embarked S':
        lis.extend([0,0,1])

    if request.GET['age'] == 'Adult':
        lis.extend([1,0,0,0,0,0])
    elif request.GET['age'] == 'Baby':
        lis.extend([0,1,0,0,0,0])
    elif request.GET['age'] == 'Child':
        lis.extend([0,0,1,0,0,0])
    elif request.GET['age'] == 'Elderly':
        lis.extend([0,0,0,1,0,0])
    elif request.GET['age'] == 'Young Adult':
        lis.extend([0,0,0,0,1,0])
    elif request.GET['age'] == 'Teenager':
        lis.extend([0,0,0,0,0,1])   

    if request.GET['title'] == 'Master':
        lis.extend([1,0,0,0,0])
    elif request.GET['title'] == 'Miss':
        lis.extend([0,1,0,0,0])
    elif request.GET['title'] == 'Mr':
        lis.extend([0,0,1,0,0])
    elif request.GET['title'] == 'Mrs':
        lis.extend([0,0,0,1,0])
    elif request.GET['title'] == 'Other':
        lis.extend([0,0,0,0,1]) 

    df.loc[0,:] = lis
    ans = cls.predict(df)
    if ans == 0:
        ans = "Dead"
    else:
        ans="Survived"

    return render(request, "ml/ml_result.html",{'ans':ans})


