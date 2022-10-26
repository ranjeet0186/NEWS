from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib import messages
from django.http.response import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import*
from frontend.models import*


# Create your views here.
def index(request): 
	form_pic=AdminProfile_Picture.objects.all()
	totalmissions=Services.objects.all().count()
	totalmembers=User.objects.all().count()
	totalconatctrequest=Contact_Us.objects.all().count()
	all_contacts=Contact_Us.objects.all()
	data={}
	data['all_contacts']=all_contacts
	data['totalmissions']=totalmissions
	data['totalconatctrequest']=totalconatctrequest
	data['totalmembers']=totalmembers
	data['form_pic']=form_pic
	return render(request,'admin/index.html',data)

@login_required
def add_services(request):
	if request.method == 'POST':
		form = ServicesForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added Service ')
			return redirect('/backend/service_view')
	else:
		form = ServicesForm()
	return render(request,'admin/services/add_services.html',{'form' : form})

@login_required
def service_view(request):
	all_services=Services.objects.all()
	data={}
	data['all_services']=all_services		
	return render(request,'admin/services/services_view.html',data)	

@login_required
def service_edit(request,pk):
	service=Services.objects.get(id=pk)
	form=ServicesForm(instance=service)
	if request.method =='POST':
		form=ServicesForm(request.POST,request.FILES,instance=service)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted Service ')
			return redirect('/backend/service_view')
	context={'form':form}
	return render(request,'admin/services/add_services.html',context)
		

@login_required
def delete_service(request,pk):
    services=Services.objects.get(id=pk)
    services.delete()
    messages.success(request, 'You successfully Deleted Service')   
    return redirect('service_view') 


# gallery
@login_required
def add_gallery(request):
	if request.method == 'POST':
		form = GalleryForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added File ')
			return redirect('/backend/gallery_view')
	else:
		form = GalleryForm()
	return render(request,'admin/add_gallery.html',{'form' : form})

@login_required
def gallery_view(request):
	all_gallery_img= Gallaery.objects.all()
	data={}
	data['all_gallery_img']=all_gallery_img		
	return render(request,'admin/admin_gallary.html',data)


@login_required
def gallery_edit(request,pk):
	gallery=Gallaery.objects.get(id=pk)
	form=GalleryForm(instance=gallery)
	if request.method =='POST':
		form=GalleryForm(request.POST,request.FILES,instance=gallery)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted File ')
			return redirect('/backend/gallery_view')

	context={'form':form}
	return render(request,'admin/add_gallery.html',context)
		

@login_required
def delete_gallery(request,pk):
    gallery=Gallaery.objects.get(id=pk)
    gallery.delete()
    messages.success(request, 'You successfully Deleted File')
    return redirect('gallery_view')


# OurTeam
@login_required
def add_our_team(request):
	if request.method == 'POST':
		form = OurTeamForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added File ')
			return redirect('/backend/our_team_view')
	else:
		form = OurTeamForm()
	return render(request,'admin/add_our_team.html',{'form' : form})

@login_required
def our_team_view(request):
	all_our_team=  OurTeam.objects.all()
	data={}
	data['all_our_team']=all_our_team		
	return render(request,'admin/our_team_view.html',data)	

@login_required
def our_team_edit(request,pk):
	our_team=OurTeam.objects.get(id=pk)
	form=OurTeamForm(instance=our_team)
	if request.method =='POST':
		form=OurTeamForm(request.POST,request.FILES,instance=our_team)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted File ')
			return redirect('/backend/our_team_view')

	context={'form':form}
	return render(request,'admin/add_our_team.html',context)
		


@login_required
def delete_our_team(request,pk):
    our_team= OurTeam.objects.get(id=pk)
    our_team.delete()
    messages.success(request, 'You successfully Deleted File')
    return redirect('our_team_view')


@login_required
def our_team_status(request,pk):
	our_team=OurTeam.objects.get(id=pk)
	form=OurTeamForm(instance=our_team)
	if request.method =='POST':
		status=request.POST['status']
		form=OurTeamForm(status=status)
		if form.is_valid():
			form.save()
			messages.success(request, 'You updated status ')
			return redirect('/backend/our_team_view')

	context={'form':form}
	return render(request,'admin/our_team_view.html',context)

# Our Testimonial
@login_required
def add_testimonial(request):
	if request.method == 'POST':
		form = OurTestimonialForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added Testimonial ')
			return redirect('/backend/testimonial_view/')
	else:
		form = OurTestimonialForm()
	return render(request,'admin/add_testimonial.html',{'form' : form})

@login_required
def testimonial_view(request):
	all_testimonial = OurTestimonial.objects.all()
	data={}
	data['all_testimonial']=all_testimonial		
	return render(request,'admin/testimonial_view.html',data)	

@login_required
def testimonial_edit(request,pk):
	testmonial=OurTestimonial.objects.get(id=pk)
	form=OurTestimonialForm(instance=testmonial)
	if request.method =='POST':
		form=OurTestimonialForm(request.POST,request.FILES,instance=testmonial)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted Testimonial ')
			return redirect('/backend/testimonial_view/')

	context={'form':form}
	return render(request,'admin/add_testimonial.html',context)
		


@login_required
def delete_testimonial(request,pk):
    testimonial= OurTestimonial.objects.get(id=pk)
    testimonial.delete()
    messages.success(request, 'You successfully Deleted File')
    return redirect('testimonial_view')

@login_required
def add_ourpartners(request):
	if request.method == 'POST':
		form = OurPartnersForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added partner ')
			return redirect('/backend/ourpartners_view/')
	else:
		form = OurPartnersForm()
	return render(request,'admin/add_ourpartners.html',{'form' : form})

@login_required
def ourpartners_view(request):
	all_ourpartners = OurPartners.objects.all()
	data={}
	data['all_ourpartners']=all_ourpartners		
	return render(request,'admin/ourpartners_view.html',data)	

@login_required
def ourpartners_edit(request,pk):
	ourpartners=OurPartners.objects.get(id=pk)
	form=OurPartnersForm(instance=ourpartners)
	if request.method =='POST':
		form=OurPartnersForm(request.POST,request.FILES,instance=ourpartners)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted partners ')
			return redirect('/backend/ourpartners_view/')

	context={'form':form}
	return render(request,'admin/add_ourpartners.html',context)
		


@login_required
def delete_ourpartners(request,pk):
    ourpartners= OurPartners.objects.get(id=pk)
    ourpartners.delete()
    messages.success(request, 'You successfully Deleted File')
    return redirect('ourpartners_view')
# Donate Now
@login_required
def add_donationdetail(request):
	if request.method == 'POST':
		form = DonateNowForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Added donation Detail ')
			return redirect('/backend/donationdetail_view/')
	else:
		form = DonateNowForm()
	return render(request,'admin/adddonationdetail.html',{'form' : form})

@login_required
def donationdetail_view(request):
	all_donationdetail = DonateDetail.objects.all()
	data={}
	data['all_donationdetail']=all_donationdetail		
	return render(request,'admin/donationdetail.html',data)	

@login_required
def donationdetail_edit(request,pk):
	Donateuser=DonateDetail.objects.get(id=pk)
	form=DonateNowForm(instance=Donateuser)
	if request.method =='POST':
		form=DonateNowForm(request.POST,request.FILES,instance=Donateuser)
		if form.is_valid():
			form.save()
			messages.success(request, 'You successfully Upadted donation detail ')
			return redirect('/backend/donationdetail_view/')

	context={'form':form}
	return render(request,'admin/adddonationdetail.html',context)
		


@login_required
def delete_donationdetail(request,pk):
    donateuser= DonateDetail.objects.get(id=pk)
    donateuser.delete()
    messages.success(request, 'You successfully Deleted Donation details')    
    return redirect('donationdetail_view')





	




	
	
	

