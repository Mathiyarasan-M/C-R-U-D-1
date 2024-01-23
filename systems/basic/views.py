from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from.models import Student
# Create your views here.
def index(request):
    mydata=Student.objects.all()
    if(mydata!=''):
        return render(request,'index.html',{'data':mydata})
    else:
        return render(request,'index.html')
    



def insertData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        obj=Student()
        obj.name=name 
        obj.email=email
        obj.age=age
        obj.gender=gender
        obj.save()
        mydata=Student.objects.all()
        return redirect('index')
    
    return render(request, 'index.html')


def updateData(request,id):
    mydata=Student.objects.get(id=id)
    if request.method == 'POST':

      name=request.POST.get('name')
      email=request.POST.get('email')
      age=request.POST.get('age')
      gender=request.POST.get('gender')

      mydata.name=name
      mydata.email=email
      mydata.age=age
      mydata.gender=gender
      mydata.save()
      return redirect('index')
    return render(request,'edit.html',{'data':mydata})


def deleteData(request,id):
    mydata=Student.objects.get(id=id)
    mydata.delete()
    return redirect('index')
