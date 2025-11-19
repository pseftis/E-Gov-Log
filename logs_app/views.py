from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .models import Profile, LogFile
from .forms import RegisterForm, OTPForm, PersonalDetailsForm, LogUploadForm

import random

# ----------------------------------------
# HOME PAGE
# ----------------------------------------
def home(request):
    return render(request, "home.html")


# ----------------------------------------
# REGISTER (STEP 1 - USERNAME, EMAIL, PASSWORD)
# ----------------------------------------
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            request.session['reg_username'] = form.cleaned_data['username']
            request.session['reg_email'] = form.cleaned_data['email']
            request.session['reg_password'] = form.cleaned_data['password']

            otp = random.randint(100000, 999999)
            request.session['reg_otp'] = str(otp)

            print("OTP (Debug):", otp)  # Show OTP in console

            messages.success(request, "OTP sent to email (Check console for now).")
            return redirect("verify_otp")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


# ----------------------------------------
# VERIFY OTP (STEP 2)
# ----------------------------------------
def verify_otp(request):
    if request.method == "POST":
        form = OTPForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            session_otp = request.session.get('reg_otp')

            if entered_otp == session_otp:
                user = User.objects.create_user(
                    username=request.session['reg_username'],
                    email=request.session['reg_email'],
                    password=request.session['reg_password']
                )
                user.save()
                login(request, user)
                return redirect("personal_details")
            else:
                messages.error(request, "Invalid OTP. Try again.")
                return redirect("verify_otp")
    else:
        form = OTPForm()

    return render(request, "verify_otp.html", {"form": form})


# ----------------------------------------
# PERSONAL DETAILS (STEP 3)
# ----------------------------------------
@login_required
def personal_details(request):
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Registration complete!")
            return redirect("dashboard")
    else:
        form = PersonalDetailsForm()

    return render(request, "personal_details.html", {"form": form})


# ----------------------------------------
# DASHBOARD (AFTER LOGIN)
# ----------------------------------------
@login_required
def dashboard(request):
    logs = LogFile.objects.filter(uploaded_by=request.user)
    return render(request, "dashboard.html", {"logs": logs})


# ----------------------------------------
# UPLOAD LOG FILES
# ----------------------------------------
@login_required
def upload_log(request):
    if request.method == "POST":
        form = LogUploadForm(request.POST, request.FILES)
        if form.is_valid():
            log = form.save(commit=False)
            log.uploaded_by = request.user
            log.save()
            messages.success(request, "Log uploaded successfully!")
            return redirect("dashboard")
    else:
        form = LogUploadForm()

    return render(request, "upload_log.html", {"form": form})
