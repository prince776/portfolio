from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages

from .models import Skill, Project, Job, Me


def home(request):
    top_skills = Skill.objects.order_by('-skill_priority')[:3]
    top_projects = Project.objects.order_by('-project_priority')[:3]

    total_skills = Skill.objects.count()
    total_projects = Project.objects.count()
    total_jobs = Job.objects.count()

    me = Me.objects.filter(active=True)[0]

    context = {
        'top_skills': top_skills,
        'top_projects': top_projects,
        'total_skills': total_skills,
        'total_projects': total_projects,
        'total_jobs': total_jobs,
        'me': me,
    }

    return render(request, 'aboutme/home.html', context)


def about(request):
    total_skills = Skill.objects.count()
    total_projects = Project.objects.count()
    total_jobs = Job.objects.count()

    me = Me.objects.filter(active=True)[0]

    context = {
        'total_skills': total_skills,
        'total_projects': total_projects,
        'total_jobs': total_jobs,
        'me': me,
    }

    return render(request, 'aboutme/about.html', context)


def skills(request):
    skills = Skill.objects.order_by('-skill_priority')

    context = {
        'skills': skills
    }

    return render(request, 'aboutme/skills.html', context)


def projects(request):
    projects = Project.objects.order_by('-project_priority')

    context = {
        'projects': projects
    }

    return render(request, 'aboutme/projects.html', context)


def jobs(request):
    jobs_done = Job.objects.filter(completed=True).order_by('-job_priority')
    jobs_current = Job.objects.filter(
        completed=False).order_by('-job_priority')

    context = {
        'jobs_done': jobs_done,
        'jobs_current': jobs_current
    }

    return render(request, 'aboutme/jobs.html', context)


def contact(request):
    me = Me.objects.filter(active=True)[0]

    context = {
        'me': me
    }

    return render(request, 'aboutme/contact.html', context)


def mail_to_me(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('aboutme:contact'))

    me = Me.objects.filter(active=True)[0]
    subject = request.POST['subject']
    message = request.POST['message']
    name = request.POST['name']
    email = request.POST['email']
    message += " sent by: " + name + ", contact: " + email

    if (not subject) or (not message) or (not name) or (not email):
        messages.warning(request, "Please enter all details!")
        return HttpResponseRedirect(reverse('aboutme:contact'))
    else:
        send_mail(subject, message,
                  'accverf007@gmail.com', [me.email],
                  fail_silently=False)
        # send message that email has been sent
        messages.success(request, "Your mail has been sent!")
        return HttpResponseRedirect(reverse('aboutme:contact'))
