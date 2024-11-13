from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import os
from .models import Skill, Experience, Academic, Project, Certificate
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
import requests
# Create your views here.

def index(request):
    
    # skills
    skills_by_category = {}
    for skill in Skill.objects.all().order_by('category'):
        category = skill.category
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    # experience
    experiences = Experience.objects.all()

    # academics
    academics = Academic.objects.all().order_by("-id")

    # projects
    projects = Project.objects.all()

    # Certificates
    certificates = Certificate.objects.all().order_by("id")
    # for certificate in certificates:
    #     print(certificate.id)

    context = {
        'skills_by_category': skills_by_category,
        'experiences': experiences,
        'academics': academics,
        'projects': projects,
        'certificates': certificates,
    }

    return render(request, "index.html", context)
