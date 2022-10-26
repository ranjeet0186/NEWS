
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'), 
       
      #services
    path('add_service/',views.add_services,name="add_service"),
    path('service_view/',views.service_view,name="service_view"),
    path('service_edit/<str:pk>/',views.service_edit,name="service_edit"),
    path('delete_service/<str:pk>/',views.delete_service,name="delete_service"),


     # gallery
    path('add_gallery/',views.add_gallery,name="add_gallery"),
    path('gallery_view/',views.gallery_view,name="gallery_view"),
    path('gallery_edit/<str:pk>/',views.gallery_edit,name="gallery_edit"),
    path('delete_gallery/<str:pk>/',views.delete_gallery,name="delete_gallery"),


     # OurTeam
    path('add_our_team/',views.add_our_team,name="add_our_team"),
    path('our_team_view/',views.our_team_view,name="our_team_view"),
    path('our_team_edit/<str:pk>/',views.our_team_edit,name="our_team_edit"),
    path('delete_our_team/<str:pk>/',views.delete_our_team,name="delete_our_team"),
    path('our_team_status/<str:pk>/',views.our_team_status,name='our_team_status'),

     # OurTeam
    path('add_testimonial/',views.add_testimonial,name="add_testimonial"),
    path('testimonial_view/',views.testimonial_view,name="testimonial_view"),
    path('testimonial_edit/<str:pk>/',views.testimonial_edit,name="testimonial_edit"),
    path('delete_testimonial/<str:pk>/',views.delete_testimonial,name="delete_testimonial"),

    #ourPartners
    path('add_ourpartners/',views.add_ourpartners,name="add_ourpartners"),
    path('ourpartners_view/',views.ourpartners_view,name="ourpartners_view"),
    path('ourpartners_edit/<str:pk>/',views.ourpartners_edit,name="ourpartners_edit"),
    path('delete_ourpartners/<str:pk>/',views.delete_ourpartners,name="delete_ourpartners"),

    # DonateNow
    path('add_donationdetail/',views.add_donationdetail,name="add_donationdetail"),
    path('donationdetail_view/',views.donationdetail_view,name="donationdetail_view"),
    path('donationdetail_edit/<str:pk>/',views.donationdetail_edit,name="donationdetail_edit"),
    path('delete_donationdetail/<str:pk>/',views.delete_donationdetail,name="delete_donationdetail"),
   
   
   
    ]