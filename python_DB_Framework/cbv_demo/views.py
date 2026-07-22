from django.shortcuts import render
from django.views.generic import TemplateView, View, FormView
from django.http import JsonResponse
from django.urls import reverse_lazy
from .models import Message
from .forms import ContactForm
import random

class HomeView(TemplateView):
    template_name = 'cbv_demo/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Randomly pick a message from the database
        messages = list(Message.objects.all())
        if messages:
            context['random_message'] = random.choice(messages).content
        else:
            context['random_message'] = "No messages available yet."
        return context

class AboutUsView(TemplateView):
    template_name = 'cbv_demo/about.html'

class CourseAPIView(View):
    def get(self, request, *args, **kwargs):
        courses = [
            {'name': 'Python for Beginners', 'price': 49.99},
            {'name': 'Django Masterclass', 'price': 79.99},
            {'name': 'React Frontend Development', 'price': 59.99},
        ]
        return JsonResponse({'courses': courses})

class ContactView(FormView):
    template_name = 'cbv_demo/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('cbv_home')

    def form_valid(self, form):
        # We can add a success message via messages framework or just pass it in context
        # FormView redirects to success_url on form_valid
        # To show success on the same page, we can override this or use messages
        return render(self.request, self.template_name, {'form': self.get_form(), 'success': True})
