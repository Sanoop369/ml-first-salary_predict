from django.shortcuts import render
import joblib
def home(request): 
    data=joblib.load('slr.sav')
    if request.method == "POST":
        h=float(request.POST["height"])

        w=data.predict([[h]])
        return render(request,'index.html',{'w':round(w[0])})


    return render(request,'index.html')