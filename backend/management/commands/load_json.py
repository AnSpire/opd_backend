import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from backend.models import UserProfile, Social, Project, Service, Experience, Education, Language, Framework, Other, Resume

class Command(BaseCommand):
    help = 'Load profile data from JSON file'

    def handle(self, *args, **kwargs):
        # Load data from JSON file
        file_path = os.path.join(os.path.dirname(__file__), 'portfolio.json')
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Create User and UserProfile
        user, created = User.objects.get_or_create(id=1)
        user_profile, created = UserProfile.objects.get_or_create(
            user=user,
            header_tagline_one=data['headerTaglineOne'],
            header_tagline_two=data['headerTaglineTwo'],
            header_tagline_three=data['headerTaglineThree'],
            header_tagline_four=data['headerTaglineFour'],
            show_cursor=data['showCursor'],
            show_blog=data['showBlog'],
            dark_mode=data['darkMode'],
            show_resume=data['showResume'],
            about_para=data['aboutpara']
        )

        # Create Social links
        for social in data['socials']:
            Social.objects.create(
                user_profile=user_profile,
                title=social['title'],
                link=social['link']
            )

        # Create Projects
        for project in data['projects']:
            Project.objects.create(
                user_profile=user_profile,
                title=project['title'],
                description=project['description'],
                image_src=project['imageSrc'],
                url=project['url']
            )

        # Create Services
        for service in data['services']:
            Service.objects.create(
                user_profile=user_profile,
                title=service['title'],
                description=service['description']
            )

        # Create Resume
        resume_data = data['resume']
        resume, created = Resume.objects.get_or_create(
            user_profile=user_profile,
            tagline=resume_data['tagline'],
            description=resume_data['description'],
            about_para=data['aboutpara']
        )

        # Create Experiences
        for experience in resume_data['experiences']:
            Experience.objects.create(
                resume=resume,
                dates=experience['dates'],
                type=experience['type'],
                position=experience['position'],
                bullets=experience['bullets']
            )

        # Create Education
        education_data = resume_data['education']
        Education.objects.create(
            resume=resume,
            university_name=education_data['universityName'],
            university_date=education_data['universityDate'],
            university_para=education_data['universityPara']
        )

        # Create Languages
        for language in resume_data['languages']:
            Language.objects.create(
                resume=resume,
                name=language
            )

        # Create Frameworks
        for framework in resume_data['frameworks']:
            Framework.objects.create(
                resume=resume,
                name=framework
            )

        # Create Others
        for other in resume_data['others']:
            Other.objects.create(
                resume=resume,
                name=other
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded profile data'))
