# your_app/management/commands/import_portfolio.py

import json
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from backend.models import Social, Project, Service, Experience, Education, Language, Framework, Other, Resume, \
    UserProfile


class Command(BaseCommand):
    help = 'Import portfolio data from portfolio.json'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(os.path.dirname(__file__), 'portfolio.json')

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        user, created = User.objects.get_or_create(username=data['name'])

        profile_data = {
            'header_tagline_one': data['headerTaglineOne'],
            'header_tagline_two': data['headerTaglineTwo'],
            'header_tagline_three': data['headerTaglineThree'],
            'header_tagline_four': data['headerTaglineFour'],
            'show_cursor': data['showCursor'],
            'show_blog': data['showBlog'],
            'dark_mode': data['darkMode'],
            'show_resume': data['showResume']
        }

        profile, created = UserProfile.objects.get_or_create(user=user, defaults=profile_data)

        if not created:
            for key, value in profile_data.items():
                setattr(profile, key, value)
            profile.save()

        resume_data = {
            'user': user,
            'tagline': data['resume']['tagline'],
            'description': data['resume']['description'],
            'about_para': data['aboutpara'],
        }

        resume, created = Resume.objects.get_or_create(user=user, defaults=resume_data)

        if not created:
            for key, value in resume_data.items():
                setattr(resume, key, value)
            resume.save()

        self.import_socials(data['socials'], user)
        self.import_projects(data['projects'], user)
        self.import_services(data['services'], user)
        self.import_experiences(data['resume']['experiences'], user)
        self.import_education(data['resume']['education'], user)
        self.import_languages(data['resume']['languages'], user)
        self.import_frameworks(data['resume']['frameworks'], user)
        self.import_others(data['resume']['others'], user)

        self.stdout.write(self.style.SUCCESS('Successfully imported portfolio data'))

    def import_socials(self, socials, user):
        for social in socials:
            Social.objects.update_or_create(
                id=int(social['id']),
                defaults={
                    'title': social['title'],
                    'link': social['link'],
                    'user': user
                }
            )

    def import_projects(self, projects, user):
        for project in projects:
            Project.objects.update_or_create(
                id=int(project['id']),
                defaults={
                    'title': project['title'],
                    'description': project['description'],
                    'image_src': project['imageSrc'],
                    'url': project['url'],
                    'user': user
                }
            )

    def import_services(self, services, user):
        for service in services:
            Service.objects.update_or_create(
                id=int(service['id']),
                defaults={
                    'title': service['title'],
                    'description': service['description'],
                    'user': user
                }
            )

    def import_experiences(self, experiences, user):
        for experience in experiences:
            Experience.objects.update_or_create(
                id=experience['id'],
                defaults={
                    'dates': experience['dates'],
                    'type': experience['type'],
                    'position': experience['position'],
                    'bullets': experience['bullets'],
                    'user': user
                }
            )

    def import_education(self, education, user):
        Education.objects.update_or_create(
            user=user,
            defaults={
                'university_name': education['universityName'],
                'university_date': education['universityDate'],
                'university_para': education['universityPara']
            }
        )

    def import_languages(self, languages, user):
        for language in languages:
            Language.objects.update_or_create(
                name=language,
                defaults={'user': user}
            )

    def import_frameworks(self, frameworks, user):
        for framework in frameworks:
            Framework.objects.update_or_create(
                name=framework,
                defaults={'user': user}
            )

    def import_others(self, others, user):
        for other in others:
            Other.objects.update_or_create(
                name=other,
                defaults={'user': user}
            )
