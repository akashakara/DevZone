from .models import Project
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    latest_projects = [(project, project.project_desc[:250]) for project in Project.objects.order_by('-published_on')]
    context = {
        'latest_projects': latest_projects
    }
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    members = [User.objects.get(pk=profile.user_id).username for profile in project.profile_set.all()]
    project.taken_by = len(project.profile_set.all())
    context = {'project': project, 'members': members}
    if not request.user.is_anonymous:
        is_member = True if request.user.profile in project.profile_set.all() else False
        context.update({'is_member': is_member})
    project.save()  
    return render(request, 'projects/detail.html', context=context)

def members(request, project_id):
    return HttpResponse(f"You're looking at the members of project #{project_id} ")

def partake(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    member_count = len(project.profile_set.all())
    if member_count >= project.max_members:
        return HttpResponse(f"Sorry, This project already reached the Member limit!")
    else:
        request.user.profile.project = Project.objects.get(pk=project_id)
        request.user.save()
        return HttpResponse(f"You have joined the project #{project_id}")