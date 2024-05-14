from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    header_tagline_one = models.CharField(max_length=255)
    header_tagline_two = models.CharField(max_length=255)
    header_tagline_three = models.CharField(max_length=255)
    header_tagline_four = models.CharField(max_length=255)
    show_cursor = models.BooleanField()
    show_blog = models.BooleanField()
    dark_mode = models.BooleanField()
    show_resume = models.BooleanField()

class Social(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.URLField()
    user = models.ForeignKey(User, related_name='socials', on_delete=models.CASCADE)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image_src = models.URLField()
    url = models.URLField()
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='services', on_delete=models.CASCADE)

class Experience(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    dates = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    bullets = models.TextField()
    user = models.ForeignKey(User, related_name='experiences', on_delete=models.CASCADE)

class Education(models.Model):
    id = models.AutoField(primary_key=True)
    university_name = models.CharField(max_length=100)
    university_date = models.CharField(max_length=100)
    university_para = models.TextField()
    user = models.ForeignKey(User, related_name='education', on_delete=models.CASCADE)

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='languages', on_delete=models.CASCADE)

class Framework(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='frameworks', on_delete=models.CASCADE)

class Other(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='others', on_delete=models.CASCADE)

class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='resume', on_delete=models.CASCADE)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    about_para = models.TextField()
