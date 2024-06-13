from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    header_tagline_one = models.CharField(max_length=255, null=True, blank=True)
    header_tagline_two = models.CharField(max_length=255, null=True, blank=True)
    header_tagline_three = models.CharField(max_length=255, null=True, blank=True)
    header_tagline_four = models.CharField(max_length=255, null=True, blank=True)
    show_cursor = models.BooleanField(default=False)
    show_blog = models.BooleanField(default=False)
    dark_mode = models.BooleanField(default=False)
    show_resume = models.BooleanField(default=False)
    about_para = models.TextField(null=True, blank=True)

class Social(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='socials', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(null=True, blank=True)

class Project(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image_src = models.URLField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

class Service(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='services', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Experience(models.Model):
    resume = models.ForeignKey('Resume', related_name='experiences', on_delete=models.CASCADE)
    dates = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    bullets = models.TextField(null=True, blank=True)

class Education(models.Model):
    resume = models.OneToOneField('Resume', related_name='education', on_delete=models.CASCADE)
    university_name = models.CharField(max_length=100, null=True, blank=True)
    university_date = models.CharField(max_length=100, null=True, blank=True)
    university_para = models.TextField(null=True, blank=True)

class Language(models.Model):
    resume = models.ForeignKey('Resume', related_name='languages', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

class Framework(models.Model):
    resume = models.ForeignKey('Resume', related_name='frameworks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

class Other(models.Model):
    resume = models.ForeignKey('Resume', related_name='others', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)

class Resume(models.Model):
    user_profile = models.OneToOneField(UserProfile, related_name='resume', on_delete=models.CASCADE)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    about_para = models.TextField(null=True, blank=True)
