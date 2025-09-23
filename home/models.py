from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    role1 = models.CharField(max_length=100, default="Trainee")
    role2 = models.CharField(max_length=100, default="Python Developer")
    bio = models.TextField(default="I'm currently on a journey to become a Python developer.")
    profile_image = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name

# About 
class About(models.Model):
    description = models.TextField()
    skills = models.CharField(max_length=300)

    def __str__(self):
        return "About Section"
