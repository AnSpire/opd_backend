import re
from rest_framework import serializers
from .models import UserProfile, Project, Social, Service, Resume
from .models import Experience, Education
from django.contrib.auth.models import User

class CustomURLValidator(serializers.URLField):
    def to_internal_value(self, data):
        if data.startswith('mailto:'):
            if re.match(r'mailto:[\w\.-]+@[\w\.-]+', data):
                return data
            else:
                self.fail('invalid')
        return super().to_internal_value(data)

class SocialSerializer(serializers.ModelSerializer):
    link = CustomURLValidator()

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

class ResumeSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True)
    education = EducationSerializer()
    languages = serializers.ListField(child=serializers.CharField())
    frameworks = serializers.ListField(child=serializers.CharField())
    others = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Resume
        fields = '__all__'

    def create(self, validated_data):
        experiences_data = validated_data.pop('experiences', [])
        education_data = validated_data.pop('education', None)

        education = None
        if education_data:
            education = Education.objects.create(**education_data)

        resume = Resume.objects.create(education=education, **validated_data)

        for experience_data in experiences_data:
            Experience.objects.create(resume=resume, **experience_data)

        return resume

class UserProfileSerializer(serializers.ModelSerializer):
    socials = SocialSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)
    services = ServiceSerializer(many=True, required=False)
    resume = ResumeSerializer(required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'

    def create(self, validated_data):
        socials_data = validated_data.pop('socials', [])
        projects_data = validated_data.pop('projects', [])
        services_data = validated_data.pop('services', [])
        resume_data = validated_data.pop('resume', None)

        user_profile = UserProfile.objects.create(**validated_data)

        for social_data in socials_data:
            Social.objects.create(user_profile=user_profile, **social_data)
        for project_data in projects_data:
            Project.objects.create(user_profile=user_profile, **project_data)
        for service_data in services_data:
            Service.objects.create(user_profile=user_profile, **service_data)

        if resume_data:
            experiences_data = resume_data.pop('experiences', [])
            education_data = resume_data.pop('education', None)

            education = None
            if education_data:
                education = Education.objects.create(**education_data)

            resume = Resume.objects.create(education=education, **resume_data)

            for experience_data in experiences_data:
                Experience.objects.create(resume=resume, **experience_data)

            user_profile.resume = resume
            user_profile.save()

        return user_profile
