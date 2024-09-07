from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm
from .models import Inquiry  # Added Inquiry import here

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'update_project.html', {'form': form})

@login_required
def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return redirect('project_list')

@login_required
def dashboard(request):
    inquiries = Inquiry.objects.all()
    return render(request, 'dashboard.html', {'inquiries': inquiries})

def home(request):
    return render(request, 'home.html')
def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})