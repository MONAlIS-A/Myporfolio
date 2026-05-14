from django.shortcuts import render
from . models import Projects_list, Personal_Info, Skill, Blog

# Create your views here.
def Home(request):
    projects = Projects_list.objects.all()
    data = Personal_Info.objects.all()
    skills = Skill.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'app/index.html', {
        'project': projects,
        'data': data,
        'skills': skills,
        'blogs': blogs
    })

def About(request):
    data = Personal_Info.objects.all()
    return render(request, 'app/about.html', {'data': data})

def Projects(request):
    projects = Projects_list.objects.all()
    data = Personal_Info.objects.all()
    return render(request, 'app/projects.html', {'projects': projects, 'data': data})

def Skills(request):
    skills = Skill.objects.all()
    data = Personal_Info.objects.all()
    return render(request, 'app/skills.html', {'skills': skills, 'data': data})

def Blogs(request):
    blogs = Blog.objects.all()
    data = Personal_Info.objects.all()
    return render(request, 'app/blog.html', {'blogs': blogs, 'data': data})

def Contact(request):
    data = Personal_Info.objects.all()
    return render(request, 'app/contact.html', {'data': data})
