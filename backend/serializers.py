from rest_framework import serializers
from .models import UserProfile, Project, Social, Service, Resume, Experience, Education, Language, Framework, Other
from django.contrib.auth.models import User

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class FrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Framework
        fields = '__all__'

class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True)
    education = EducationSerializer()
    languages = LanguageSerializer(many=True)
    frameworks = FrameworkSerializer(many=True)
    others = OtherSerializer(many=True)

    class Meta:
        model = Resume
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    socials = SocialSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    resume = ResumeSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'
