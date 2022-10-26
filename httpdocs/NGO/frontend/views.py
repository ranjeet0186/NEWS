from django.shortcuts import render

from backendapp2.models import*

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import (get_object_or_404,  render,redirect, HttpResponseRedirect)
from django.http import HttpResponse, request
from frontend.forms import*
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.urls import reverse_lazy
from math import ceil
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    all_contact_details= Contact_Deatails.objects.all()
    all_ourpartners= OurPartners.objects.all()
    p=len(all_ourpartners)
    pSlides=p//5+ceil((p/5)-(p//5))

    print( all_ourpartners)

    all_services= Services.objects.all()
    n=len(all_services)
    nSlides=n//4+ceil((n/4)-(n//4))

    all_gallery= Gallaery.objects.all()
    g=len(all_gallery)   
    gSlides=g//4+ceil((g/4)-(g//4))

    all_testimonials=OurTestimonial.objects.all()
    print(all_testimonials)
    t=len(all_testimonials)
    tSlides= t//4 + ceil((t/4) + (t//4))
      
   
    data={ 'all_services':all_services,'all_contact_details':all_contact_details, 'no_of_slides':nSlides,'range':range(1,nSlides), 'no_of_gslides':gSlides,'grange':range(1,gSlides),'all_gallery':all_gallery,'no_of_tslides':tSlides,'trange':range(1,tSlides),'all_testimonials':all_testimonials,'no_of_pslides':pSlides,'prange':range(1,pSlides),'all_ourpartners': all_ourpartners,}
    return render(request,'frontend/index.html',data)

def about(request):
    all_contact_details= Contact_Deatails.objects.all()
    data={}
    data['all_contact_details']=all_contact_details
    return render(request,'frontend/about.html',data)


    

def contact(request):
    all_contact_details= Contact_Deatails.objects.all()
    data={}
    data['all_contact_details']=all_contact_details    
    if request.method =='POST':
        Name=request.POST['Name']
        email=request.POST['email']
        contact=request.POST['mobile']
        message=request.POST['messages']
        try:
            Contact_Us.objects.create(Name=Name,email=email,mobile=contact,messages=message) 
            messages.success(request,'Your message successfully sent ..')                   
            return redirect('contact')
        except:
            messages.success(request,'something went wrong,try again...')                
            return redirect('contact')
    return render(request,'frontend/contact.html',data)


def contact_view(request):    
    all_contacts= Contact_Us.objects.all()
    data={}
    data['all_contacts']=all_contacts       
    return render(request,'admin/contact_view.html',data)  

def delete_contact(request,pk):
    delete_contact= Contact_Us.objects.get(id=pk)
    delete_contact.delete()
    messages.success(request, 'You successfully deleted this messages')
    return redirect('contact_view')

def our_team(request):
    all_team= OurTeam.objects.all()
    all_contact_details= Contact_Deatails.objects.all()
    data={}
    data['all_team']=all_team
    data['all_contact_details']=all_contact_details  
    return render(request,'frontend/our_team.html',data)

def OurProjects(request):
    all_contact_details= Contact_Deatails.objects.all()
    all_gallery= Gallaery.objects.all()
    data={}
    data['all_contact_details']=all_contact_details
    data['all_gallery']=all_gallery
    return render(request,'frontend/OurProjects.html',data)

def our_mission(request): 
    all_contact_details= Contact_Deatails.objects.all()
    all_services= Services.objects.all()
    data={}
    data['all_contact_details']=all_contact_details
    data['all_services']=all_services   
    return render(request,'frontend/our_mission.html',data)

def our_mission_view(request,id):
    service_view=Services.objects.filter(id=id)[0] 
    all_contact_details= Contact_Deatails.objects.all()
    all_services= Services.objects.all()
    data={}
    data['all_contact_details']=all_contact_details
    data['all_services']=all_services  
    data['service_view']=service_view   
    return render(request,'frontend/our_mission_view.html',data)

@login_required
def user_dashboard_view(request,pk):    
    if not request.user.is_authenticated:
        return redirect('login')
    error=""    
    member=Members.objects.get(id=pk)
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contact=request.POST['contact']
        email=request.POST['email']
        gender=request.POST['gender']

        member.user.first_name=firstname
        member.user.last_name=lastname
        member.mobile=contact
        member.user.username=email
        member.gender=gender
        try:
            member.user.save()
            member.save()
            error='no'
        except:
            error='yes'        
    d={'error':error,'member':member}
    return render(request,'admin/user_profile.html',d) 
@login_required
def change_profile_picture(request,pk):    
    if not request.user.is_authenticated:
        return redirect('login')
    error=""    
    member=Members.objects.get(id=pk)
    if request.method =='POST':
        image=request.FILES['image']
        member.image=image       
        try:           
            member.save()
            error='no'
        except:
           error='yes'    
        
    d={ 'error':error,'member':member}
    return render(request,'admin/change_profile picture.html',d)                        
@login_required
def user_dashboard(request):    
    return render(request,'frontend/user_dashboard.html',)    
@login_required
def user_profile(request):
    user=request.user
    error =""
    if request.method =='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contact=request.POST['contact']
        email=request.POST['email']
        gender=request.POST['gender']   
        

        user.first_name=firstname
        user.last_name=lastname
        user.username=email
        user.members.mobile=contact
        user.members.gender=gender
        
        try:
            user.members.save()
            user.save()
            messages.success(request, 'You successfully updated profile ')
            return redirect('user_profile')
        except:
            messages.success(request, 'Something Went worng ,try again')
            return redirect('user_profile')        
    d={'user':user}
    return render(request,'frontend/user_profile.html',d)  
@login_required
def user_profile_picture(request):
    user=request.user
    error =""
    if request.method =='POST':
        image=request.FILES['image']       
        user.members.image=image
        
        try:
            user.members.save()
            messages.success(request, 'You successfully updated profile picture')
            return redirect('user_profile')
        except:
            messages.success(request, 'Something Went worng ,try again')
            return redirect('user_profile')
        
    d={'user':user}
    return render(request,'frontend/change_userprofile_picture.html',)      
@login_required
def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""   
    if request.method=='POST':
        c=request.POST['currentpassword']
        n=request.POST['newpassword']        
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()           
                messages.success(request, 'You successfully changed password')
                return redirect('login')
            else:
                messages.success(request, 'Your current password does not match ,try again')
                return redirect('change_passworduser')       
        except:
            messages.success(request, 'Something Went worng ,try again')
            return redirect('user_profile')       
    return render(request,'frontend/change_passworduser.html')       



