from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name



from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='technologies/')  # store tech icons in /media/technologies/

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    github_link = models.URLField()
    live_link = models.URLField()
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)

    def __str__(self):
        return self.title



class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/")

    def __str__(self):
        return f"{self.project.title} Image"

