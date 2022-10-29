from django.shortcuts import render

# Create your views here.
def homepage(request):
     return render(request,'Operations/homepage.html')
 
def projects(request):
    return render(request,'Operations/projects.html')

def anouncement(request):
    return render(request,'Operations/anouncements.html')
