# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from .forms import GoalForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    goals = Goal.objects.all()
    return render (request, 'index.html', {"goals":goals})

def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST, request.FILES)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.save()
            # return HttpResponseRedirect(goal.get_absolute_url())
        return redirect('index')
    else:
        form = GoalForm() 
    return render(request, 'add_goal.html', {"form": form})

def goal_detail(request, id):
    goals = Goal.objects.get(id=id)
    return render( request, 'goal_detail.html' , {"goals":goals})
    
def goal_update(request, id):
    goal = get_object_or_404(Goal, pk=id)
    form = GoalForm(request.POST, instance= goal)
    context ={
        "goal": goal,
        "form": GoalForm(instance=goal)
    }
    if form.is_valid():
        goal = form.save(commit=False)
        goal.save()
        return redirect('index')
    return render (request, 'update_form.html', context)

def goal_delete(request, id):
    goal = get_object_or_404(Goal, id=id)
    if request.method == "POST":
        # confirm delete
        goal.delete()
        return redirect('index')
    context = {
        "goal": goal
    }
    return render(request, 'delete_goal.html', context)
