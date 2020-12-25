from django.shortcuts import render,HttpResponse
import joblib

# Create your views here.

def fifa(request):
	return render(request,'fifa.html')

def result(request):
	prediction=joblib.load('model_fifa.sav')
	x=[]
	x.append(request.GET['Age'])
	x.append(request.GET['Crossing'])
	x.append(request.GET['Finishing'])
	x.append(request.GET['ShortPassing'])
	x.append(request.GET['Dribbling'])
	x.append(request.GET['Acceleration'])
	x.append(request.GET['ShotPower'])
	
	res=prediction.predict([list(map(float,x))])
	a=int(res)


	
	
	return render(request,'result.html',{'a':a})






















	


def diabetes(request):
	return render(request,'diabetes.html')

def result_diabetes(request):
	prediction=joblib.load('model_diabetes.sav')
	x=[]
	x.append(request.GET['Pregnancies'])
	x.append(request.GET['Glucose'])
	x.append(request.GET['BloodPressure'])
	x.append(request.GET['SkinThickness'])
	x.append(request.GET['Insulin'])
	x.append(request.GET['BMI'])
	x.append(request.GET['DiabetesPedigreeFunction'])
	x.append(request.GET['Age'])
	
	res=prediction.predict([list(map(float,x))])
	#print(res)
	a=int(res)
	result=""
	if a==0:
		result="Negative"
	else:
		result="Positive"


	
	
	return render(request,'result_diabetes.html',{'result':result})