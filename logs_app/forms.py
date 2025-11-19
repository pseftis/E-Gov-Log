from django import forms
from django.contrib.auth.models import User
from .models import Profile, LogFile

# ---------------------------
# REGISTER FORM (STEP 1)
# ---------------------------
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# ---------------------------
# OTP FORM (STEP 2)
# ---------------------------
class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)


# ---------------------------
# PERSONAL DETAILS FORM (STEP 3)
# ---------------------------
class PersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["full_name", "gender", "dob"]

        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "gender": forms.Select(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
        }


# ---------------------------
# FILE UPLOAD FORM
# ---------------------------
class LogUploadForm(forms.ModelForm):
    class Meta:
        model = LogFile
        fields = ["file_name", "description", "file"]
