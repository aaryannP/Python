from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import random
from .forms import ForgotPasswordForm, OTPVerificationForm

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Generate 6-digit OTP
            otp = str(random.randint(100000, 999999))
            
            # Store in session and set expiry to 5 minutes (300 seconds)
            request.session['otp'] = otp
            request.session.set_expiry(300)
            
            # Send email
            subject = 'Your Password Reset OTP'
            message = f'Your 6-digit OTP for password reset is: {otp}\nThis OTP is valid for 5 minutes.'
            from_email = settings.EMAIL_HOST_USER
            
            try:
                send_mail(subject, message, from_email, [email])
            except Exception as e:
                # Catching exceptions for local testing if SMTP isn't working perfectly, though we use console backend.
                pass
                
            return redirect('verify_otp')
    else:
        form = ForgotPasswordForm()
        
    return render(request, 'otp_system/forgot_password.html', {'form': form})

def verify_otp_view(request):
    message = None
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            session_otp = request.session.get('otp')
            
            if session_otp and entered_otp == session_otp:
                message = "Success! OTP verified."
                # Optionally clear OTP after successful verification
                del request.session['otp']
            else:
                message = "Error: Invalid or expired OTP."
    else:
        form = OTPVerificationForm()
        
    return render(request, 'otp_system/verify_otp.html', {'form': form, 'message': message})
