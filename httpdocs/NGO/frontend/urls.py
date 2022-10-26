from django.urls import path

from .import views


urlpatterns = [ 
    path('',views.index,name='home'),  
   
    path('about',views.about,name='about'),
    path('our_mission',views.our_mission,name='our_mission'),
    path('our_mission_view/<int:id>/',views.our_mission_view,name='our_mission_view'),

    path('contact',views.contact,name='contact'),
    path('contact_view/',views.contact_view,name='contact_view'),
    path('delete_contact/<str:pk>/',views.delete_contact,name="delete_contact"),
    path('our_team/',views.our_team,name='our_team'),
    path('ourprojects',views.OurProjects,name="ourprojects"),

    path('user_dashboard/',views.user_dashboard,name='user_dashboard',),
    path('user_dashboard_view/<int:pk>/',views.user_dashboard_view,name='user_dashboard_view'),
    path('change_profile_picture/<int:pk>/',views.change_profile_picture,name='change_profile_picture'),
    path('user_profile/',views.user_profile,name='user_profile') ,
    path('user_profile_picture/',views.user_profile_picture,name='user_profile_picture') ,
    path('change_passworduser/',views.change_passworduser, name="change_passworduser"),  
    
    
    ]
