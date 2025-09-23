from django.shortcuts import render
from .models import Skill
from .models import Project

def project_list(request):
    projects = Project.objects.prefetch_related("images").all()
    return render(request, "projects/projects.html", {"projects": projects})


def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'projects/skills.html', {'skills': skills})
