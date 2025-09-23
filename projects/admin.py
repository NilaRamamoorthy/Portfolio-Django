from django.contrib import admin
from .models import Skill

admin.site.register(Skill)

from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):   # or StackedInline
    model = ProjectImage
    extra = 1   # show one extra blank image upload field
    fields = ("image",)  # fields to display

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "github_link", "live_link")
    search_fields = ("title", "short_description")
    inlines = [ProjectImageInline]   # add inline images under each project

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image")
