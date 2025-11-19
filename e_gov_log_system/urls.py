from django.contrib import admin
from django.urls import path
from logs_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),     # Home Page
    path('admin/', admin.site.urls),

    # Registration / Login Flow
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('personal-details/', views.personal_details, name='personal_details'),

    # Login + Logout using our templates
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name="registration/login.html"),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Log Upload & Dashboard
    path('upload/', views.upload_log, name='upload_log'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
