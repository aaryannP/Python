from django import forms

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True)

class OTPVerificationForm(forms.Form):
    otp = forms.CharField(label='Enter OTP', max_length=6, required=True)
