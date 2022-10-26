"""NGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views
from django .conf.urls.static import static
from NGO import settings
admin.site.index_title = ''
admin.site.site_header = 'Greatemaya Foundation'
from django.conf import settings
from django.contrib.auth import views as auth_view
from .forms import MyPasswordResetForm,MySetPasswordForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='frontend/password/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='frontend/password/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='frontend/password/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='frontend/password/password_reset_complete.html'), name='password_reset_complete'),


    path('accounts/login/', views.login_call,name='login'),

   
    path('logout/', views.logout_call,name='logout'),
    path('signup/', views.signup,name='signup'),
   
   
    path('backend/',include('backendapp2.urls')),
    path('',include('frontend.urls')),

    # admin profile
    path('admin_profile/',views.admin_profile,name='admin_profile'),
    path('admin_profile_pic/<str:id>/',views.admin_profile_pic,name='admin_profile_pic'),
     path('change_passwordadmin/',views.change_passwordadmin, name="change_passwordadmin"),  


     # Clients
    
    path('client_view/',views.client_view,name='client_view'),
    path('client_edit/<str:pk>/',views.client_edit,name="client_edit"),
    path('delete_client/<str:pk>/',views.delete_client,name="delete_client"),

    # Contact-Details 
    path('contact_details_view/',views.contact_details_view,name='contact_details_view'),   
    path('add_contact_details/',views.add_contact_details,name='add_contact_details'),
    path('contact_details_edit/<str:pk>/',views.contact_details_edit,name="contact_details_edit"),
    path('delete_contact_details/<str:pk>/',views.delete_contact_details,name="delete_contact_details"),
   
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,ducument_root=settings.STATIC_DIR)

# +static(settings.MEDIA_URL,ducument_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,ducument_root=settings.STATIC_DIR)

