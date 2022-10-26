from django.shortcuts import render, redirect,HttpResponseRedirect
from backendapp2.forms import UserForm, UserProfileForm,Contact_Details_Form,AdminProfileForm,Admin_Profile_Pic_Form
from backendapp2.models import AdminProfile_Picture,Members,Contact_Deatails
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
	all_contact_details = Contact_Deatails.objects.all()	
	error =""
	if request.method =='POST':
		firstname=request.POST['firstname']
		lastname=request.POST['lastname']
		contact=request.POST['contact']
		email=request.POST['email']
		gender=request.POST['gender']	
		image=request.FILES['image']
		password1=request.POST['password1']
		try:
			user=User.objects.create_user(first_name=firstname,last_name=lastname,username=email,password=password1)
			Members.objects.create(user=user,mobile=contact,image=image,gender=gender)
			messages.success(request, 'Signup successfully !! ')
			return redirect('login')
		except:
			messages.success(request, 'Something went wrong ,Please tyr again... !! ')
			return redirect('signup')
	d={'all_contact_details':all_contact_details}
	return render(request, 'frontend/register.html',d)
	
def login_call(request):
	all_contact_details = Contact_Deatails.objects.all()
	error =""
	if request.method =='POST':
		uname=request.POST['username']
		pwd=request.POST['password']
		user=authenticate(username=uname,password=pwd)
		if user:
			try:
				if user.is_superuser:
					login(request,user)
					messages.success(request, 'Login successfully!! ')
					return redirect('index')
				else:
					user1=Members.objects.get(user=user)
					if user1:
						login(request,user)
						messages.success(request, 'Login successfully!! ')
						return redirect('user_profile')
					else:
						messages.success(request, 'Invalid Login Credentials , Try again... ')
						return redirect('login')
			except:
				messages.success(request, 'Invalid Login Credentials , Try again... ')
				return redirect('login')
		else:
			messages.success(request, 'Invalid Login Credentials , Try again... ')
			return redirect('login')
	d={'all_contact_details':all_contact_details}                      
	return render(request, 'frontend/userlogin.html',d)

@login_required
def logout_call(request):
	logout(request)
	messages.success(request, 'You Logout.. !! ')
	return redirect('login')

#admin profile chanage
@login_required
def admin_profile(request):
	admin=User.objects.all()	
	user=request.user
	form_pic=AdminProfile_Picture.objects.all()
	form=AdminProfileForm(instance=user)
	if request.method =='POST':
		form=AdminProfileForm(request.POST,request.FILES,instance=user)		
		if form.is_valid():
			form.save()			
			messages.success(request, 'You successfully updated profile !! ')
			return HttpResponseRedirect('/admin_profile/')
	context={'form':form,'admin':'admin','form_pic':form_pic}
	return render(request,'admin/adminprofile/profile.html',context) 	

@login_required
def admin_profile_pic(request,id):
	get_img=AdminProfile_Picture.objects.all()
	admin_pic=AdminProfile_Picture.objects.get(id=id)
	form_pic = Admin_Profile_Pic_Form(instance=admin_pic)
	if request.method == 'POST':
		form_pic = Admin_Profile_Pic_Form(request.POST,request.FILES,instance=admin_pic)
		if form_pic.is_valid():
			form_pic.save()
			messages.success(request, 'You successfully updated profile picture ')
			return HttpResponseRedirect('/admin_profile/')
	else:
		form_pic= Admin_Profile_Pic_Form(instance=admin_pic)
	return render(request,'admin/adminprofile/admin_pic.html',{'form_pic' : form_pic,'get_img':get_img})
def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error="" 
    form_pic=AdminProfile_Picture.objects.all()  
    if request.method=='POST':
        c=request.POST['currentpassword']
        n=request.POST['newpassword']        
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()           
                error='no'
            else:
                error="not"    
        except:
            error='yes'    
    d={'error':error,'form_pic':form_pic}
    return render(request,'admin/change_passwordadmin.html',d)




@login_required
def client_view(request):	
	all_users=Members.objects.all()
	print(all_users)
	data={}	
	data['all_users']=all_users				
	return render(request,'admin/clients_details.html',data)	



@login_required
def client_edit(request,pk):
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
	return render(request,'admin/edit_client.html',d)
		

@login_required
def delete_client(request,pk):
    if not request.user.is_authenticated:
        return redirect('login')
    client = User.objects.get(id=pk)
    client.delete()    
    return redirect('client_view')
   



 #contact-details
@login_required
def add_contact_details(request):
	if request.method == 'POST':
		form = Contact_Details_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added Contact ')
			return redirect('/contact_details_view')
	else:
		form = Contact_Details_Form()
	return render(request,'admin/add_contact_details.html',{'form' : form})

@login_required
def contact_details_view(request):
	all_contact_details= Contact_Deatails.objects.all()
	data={}
	data['all_contact_details']=all_contact_details		
	return render(request,'admin/contact_details_view.html',data)

@login_required
def contact_details_edit(request,pk):
	contact_details=Contact_Deatails.objects.get(id=pk)
	form=Contact_Details_Form(instance=contact_details)
	if request.method =='POST':
		form=Contact_Details_Form(request.POST,request.FILES,instance=contact_details)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted Contact Details ')
			return redirect('/contact_details_view')

	context={'form':form}
	return render(request,'admin/add_contact_details.html',context)
		

@login_required
def delete_contact_details(request,pk):
    contact_details= Contact_Deatails.objects.get(id=pk)
    contact_details.delete()
    messages.success(request, 'You successfully Deleted Contact Details')
    return redirect('contact_details_view')