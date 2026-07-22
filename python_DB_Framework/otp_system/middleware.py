from django.shortcuts import redirect
from django.urls import reverse

class BlockExpiredOTPAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow passing if the requested URL is not the verify page.
        # Use simple string matching or resolve URL. Here we do simple path matching.
        verify_path = '/session10/verify-otp/'
        
        if request.path == verify_path:
            # Check if OTP exists in session
            if not request.session.get('otp'):
                # Redirect back to forgot password page if OTP is missing/expired
                return redirect('forgot_password')
                
        response = self.get_response(request)
        return response
