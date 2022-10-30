from django.shortcuts import render
from . models import Project, PublicSector, PublicComment

# Create your views here.
def homepage(request):
     return render(request,'Operations/homepage.html')
 
def projects(request):
    project_list = Project.objects.all()
    
    for project in project_list:
        project_comment_list = PublicComment.objects.all().filter(project=project)
    
    
    print("comment")
    context = {
        'project_list': project_list,
        'project_comment_list': project_comment_list,
    }
    return render(request,'Operations/projects.html', context)

def anouncement(request):
    return render(request,'Operations/anouncements.html')
