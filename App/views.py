from django.shortcuts import render
from django.views import View 
from .forms import StudentRegistration
from .models import profile
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
import os
def first(request):
    profiles = profile.objects.all()  # Define and initialize profiles
    
    if request.method == 'GET':
        search = request.GET.get('search')
        if search:
            profiles = profile.objects.filter(Q(name__icontains=search) | Q(address__icontains=search))
            if  not profiles:
                 redirect('first')
        else:
            profiles = profile.objects.all()
    
    return render(request, 'first.html',locals())

def create(request):
        if request.method ==  'POST':
            name = request.POST.get('name')
            image = request.FILES.get('image')
            email = request.POST.get('email')
            age = request.POST.get('age')
            address = request.POST.get('address')
            phone_no = request.POST.get('phone_no')
            date_of_birth = request.POST.get('date_of_birth')
            religion = request.POST.get('religion')
            if  name:
                if image:
                        prof=profile.objects.create(
                            name=name, 
                            image=image,
                            email=email,
                            age=age,
                            address=address,
                            phone_no=phone_no,
                            date_of_birth=date_of_birth, 
                            religion=religion,
                            
                        )
                        prof.save()
                        messages.success(request, 'Form submitted successfully!')
                        return redirect('first')
                else:
                    prof=profile.objects.create(
                            name=name, 
                            image=image,
                            email=email,
                            age=age,
                            address=address,
                            phone_no=phone_no,
                            date_of_birth=date_of_birth, 
                            religion=religion,
                            
                            )
                    prof.save() 
                    messages.success(request, 'Form submitted successfully!')
                    return redirect('first')

        return render(request, 'create.html')


def deletedata(request,id):
   
        pi=profile.objects.get(pk=id)
        pi.delete()
        return redirect('first')


def see_profile(request,id):
        prof=profile.objects.get(pk=id)
   
       
        return render(request, 'seefullProfile.html',locals())

def update_profile(request,id):
        prof=profile.objects.get(pk=id)
        if request.method ==  'POST':
            if len(request.FILES.get('image')) !=0:
                    if prof.image != 'default/def.jpg':
                          os.remove(prof.image.path)
                   
                    name = request.POST.get('name')
                    image = request.FILES.get('image')
                    email = request.POST.get('email')
                    age = request.POST.get('age')
                    address = request.POST.get('address')
                    phone_no = request.POST.get('phone_no')
                    date_of_birth = request.POST.get('date_of_birth')
                    religion = request.POST.get('religion')
                    prof.name = name
                    prof.image = image
                    prof.email = email
                    prof.age = age
                    prof.address = address
                    prof.phone_no = phone_no
                    prof.date_of_birth = date_of_birth
                    prof.religion = religion
                    prof.save()
                    messages.success(request, 'Form updated successfully!')
                    return redirect('first')
            else:
                name = request.POST.get('name')
                image = request.FILES.get('image')
                email = request.POST.get('email')
                age = request.POST.get('age')
                address = request.POST.get('address')
                phone_no = request.POST.get('phone_no')
                date_of_birth = request.POST.get('date_of_birth')
                religion = request.POST.get('religion')
                prof.save()
                messages.success(request, 'Form updated successfully!')
                return redirect('first')
   
     
        return render(request, 'updateprofile.html',locals())    
'''
class profileView(View):
    def get(self, request):
        fm = StudentRegistration()
        stu=profile.objects.all()
        return render(request, 'profileView.html', {'form': fm,'stu':stu})
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            image = fm.cleaned_data['image']
            email = fm.cleaned_data['email']
            age = fm.cleaned_data['age']
            address = fm.cleaned_data['address']
            phone_no = fm.cleaned_data['phone_no']
            date_of_birth = fm.cleaned_data['date_of_birth']
            religion = fm.cleaned_data['religion']
            
            reg = profile(name=name, image=image, email=email, age=age, address=address, phone_no=phone_no, date_of_birth=date_of_birth, religion=religion)
            reg.save()
            
            return redirect('profileView')  # Replace 'profileView' with the appropriate URL name or path
        else:
            return render(request, 'profileView.html', {'form': fm})


class update(View):
    def get(self, request, id):
        pi = profile.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'profileView.html', {'form': fm, 'id': id})
    
    def post(self, request, id):
        pi = profile.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('profileView')  # Replace 'profileView' with the appropriate URL name or path
        else:
            return render(request, 'profileView.html', {'form': fm, 'id': id})
'''