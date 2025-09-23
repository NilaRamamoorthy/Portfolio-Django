from django.shortcuts import render
from .models import Profile, About
from projects.models import Project

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()[:4]
    print("Projects found:", projects)
    return render(request, "home/home.html", {
        "profile": profile,
        "projects": projects  # ✅ Add this line
    })



# home/views.py
def about_view(request):
    about = About.objects.first()
    return render(request, 'home/about.html', {'about': about})
