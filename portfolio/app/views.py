from django.shortcuts import render
from . models import Projects_list, Personal_Info

# Create your views here.
def Home(request):
    projects = Projects_list.objects.all()
    data = Personal_Info.objects.all()
    return render(request, 'app/index.html',{'project':projects, 'data':data})

def About(request):
    return render(request, 'app/about.html')



def Projects(request):
    projects = Projects_list.objects.all()    
    return render(request, 'app/projects.html' ,{'projects':projects})

def Contact(request):
    data = Personal_Info.objects.all()
    return render(request, 'app/contact.html', {'data':data})
