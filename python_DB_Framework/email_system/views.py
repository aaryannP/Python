from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def home(request):
    return render(request, 'email_system/home.html')

def send_password_reset_email(request, user_email='test@example.com'):
    subject = 'Reset Your Password'
    message = 'Hi there,\n\nWe received a request to reset your password. Click the link below to set a new password:\n\nhttp://localhost:8000/reset-password/\n\nIf you did not request this, please ignore this email.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse(f"Password reset email sent successfully to {user_email}.")

def trigger_password_reset(request):
    # This view acts as a trigger point since the requirement asked for a function
    # taking request and user_email. We call it here with a dummy email.
    return send_password_reset_email(request, 'customer@example.com')

def send_order_confirmation(request):
    subject = 'Your Swiggy Order Confirmation'
    from_email = settings.EMAIL_HOST_USER
    to = 'customer@example.com'
    
    # Context data for the template
    context = {
        'name': 'Aryan',
        'order_id': 'SWG-102938',
        'items': ['Margherita Pizza', 'Garlic Bread', 'Coke'],
        'total': '₹550'
    }
    
    text_content = "Thank you for your order! Your food is being prepared."
    html_content = render_to_string('email_system/order_confirmation.html', context)
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    return HttpResponse("Order confirmation HTML email sent successfully.")

def send_ipl_welcome(request):
    # AI-generated content
    subject = '🏆 Welcome to the Ultimate IPL Fantasy League! 🏏'
    text_content = 'Get ready to build your dream team and win big! The IPL Fantasy League is back.'
    
    context = {'name': 'Cricket Fan'}
    html_content = render_to_string('email_system/ipl_welcome.html', context)
    
    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, ['player@example.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    return HttpResponse("IPL Fantasy League welcome email sent successfully.")
