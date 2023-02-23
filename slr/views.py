from django.shortcuts import render
import joblib
def home(request): 
    data=joblib.load('slr.sav')
    if request.method == "POST":
        h=float(request.POST["height"])

        w=data.predict([[h]])
        return render(request,'index.html',{'w':round(w[0])})


    return render(request,'index.html')


def mlr(request): 
    data=joblib.load('mlr.sav')
    if request.method == "POST":
        area=float(request.POST["area"])
        bed=int(request.POST["bed"])
        age=int(request.POST["age"])

        w=data.predict([[area,bed,age]])
        return render(request,'index.html',{'w':round(w[0])})


    return render(request,'mlr.html')
