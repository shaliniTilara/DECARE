from django.shortcuts import render
from .models import Client
from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Client
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method =="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        city=request.POST.get("city")
        disease=request.POST.get("disease")
        Client.objects.create(
            name=name,
            email=email,
            phone=phone,
            city=city,
            disease=disease)
        return render(request,'index.html')
    return render(request,'index.html')



def doctor_create(request):
    
   if request.method=="POST":

    name=request.POST.get("name")
    specialization=request.POST.get("specialty")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    phone=request.POST.get("gender")
    gender = request.POST.get("gender")
    Doctor.objects.create(
            name=name,
            specialization=specialization,
            email=email,
            phone=phone,
            gender=gender)
    return redirect('/doctors/')
   return render(request,'doctor_form.html')   
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})
    # return HttpResponse(doctors)


def doctor_search(request):
    if request.method=="POST":
        query = request.POST.get('specialty')
        doctors = Doctor.objects.filter(specialization=query) 
        return render(request,'doctor_search.html', {'doctors': doctors})
        # return HttpResponse(doctors)
    return render(request,'doctor_search.html')

def doctor_edit(request,pk):
   doc = Doctor.objects.get(id=pk)
   if request.method=="POST":
    name=request.POST.get("name")
    specialization=request.POST.get("specialty")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    doc.name=name
    doc.specialization=specialization
    doc.email=email
    doc.phone=phone
    doc.save()
    return redirect('/doctors/')
   return render(request,'editform.html',{'doctor':doc})
def delete_doctor(request, pk):
    doctor=Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('/doctors/')
    