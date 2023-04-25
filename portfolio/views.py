from django.shortcuts import render, redirect
from .models import Project, Testimonial, Skill, Service
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def home(request):
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all().values("title", "name", "text", "image")
    skills = Skill.objects.all().values("name", "value")
    skills_length = len(skills)
    services = Service.objects.all().values("title", "text", "svg_path", "icon_box", "aos_delay", "icon_name")
    return render(request, "portfolio/home.html", 
                  {"projects": projects, "testimonials": testimonials, "skills_part1": skills[:skills_length//2], "skills_part2": skills[skills_length//2:], "services": services})

def custom_page_not_found_view(request, exception):
    print("I am here")
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            try:
                EmailMessage(f"{subject}, email from {name}",
                         message,
                         settings.ADMIN_EMAIL,
                         [settings.ADMIN_EMAIL], 
                         [], 
                         reply_to=[email] ).send()
            
                return HttpResponse("OK", status=200)
            except:
                return HttpResponse("EMAIL sent error", status=403)
        
    return HttpResponse("Form Error", status=403)
