from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, JobCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model, authenticate, login, logout
from .models import Job


# Create your views here.

def home(req):
    return render(req, 'home.html')


def user_signup(req, id):
    if req.method == 'POST':
        fm = SignUpForm(req.POST)
        if fm.is_valid():
            messages.success(req, "Account created successfully!")
            user = fm.save()
            if id==1:
                group = Group.objects.get(name = 'Terraformers')
                user.groups.add(group)
            else:
                group = Group.objects.get(name = 'Applicants')
                user.groups.add(group)
            login(req, user)
            return HttpResponseRedirect('/dashboard/%i' % id)
        else:
            messages.warning(req, "Error occured")
    else:
        fm = SignUpForm()
    return render(req, 'signup.html', {'form': fm, 'group': id})


def user_login(req, id):
    if id==1:
        user_group = Group.objects.get(name = 'Terraformers')
    else:
        user_group = Group.objects.get(name = 'Applicants')
    if req.user.is_authenticated and user_group != req.user.groups.all()[0] or not req.user.is_authenticated:
        if req.method == 'POST':
            fm = LoginForm(request=req, data=req.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=uname, password=password)
                group = user.groups.all()
                if id==1:
                    user_group = Group.objects.get(name = 'Terraformers')
                else:
                    user_group = Group.objects.get(name = 'Applicants')
                if user is not None and group[0] == user_group:
                    login(req, user)
                    messages.success(req, 'Logged in successfully!') 
                    return HttpResponseRedirect('/dashboard/%i' % id)
                else:
                    messages.warning(req, 'Please enter correct details in correct group')
        else:
            fm = LoginForm()
        return render(req, 'login.html', {'form': fm, 'group': id})
    else:
        return HttpResponseRedirect('/dashboard/%i' % id)


def user_logout(req):
    logout(req)
    return HttpResponseRedirect('/')


def dashboard(req, id):
    if id==1:
        user_group = Group.objects.get(name = 'Terraformers')
        category = 'Terraformer'
    else:
        user_group = Group.objects.get(name = 'Applicants')
        category = 'Applicant'

    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        jobs = Job.objects.all()
        jobs_user = {}
        for job in jobs:
            if Job.objects.get(pk=job.id).people.filter(id=req.user.id):
                jobs_user[job.id] = True
        return render(req, "dashboard.html", {'category': category, 'group': id, 'jobs': jobs, 'jobs_user': jobs_user})
    else:
        messages.warning(req, "You are not authorized to access this group.")
        return HttpResponseRedirect('/')


def archieved_jobs(req, id):
    if id==1:
        user_group = Group.objects.get(name = 'Terraformers')
        category = 'Terraformer'
    else:
        user_group = Group.objects.get(name = 'Applicants')
        category = 'Applicant'

    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        jobs = Job.objects.all()
        return render(req, "archieved.html", {'category': category, 'group': id, 'jobs': jobs})
    else:
        messages.warning(req, "You are not authorized to access this group.")
        return HttpResponseRedirect('/')


def add_job(req, id):
    user_group = Group.objects.get(name = 'Terraformers')

    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        if req.method == 'POST':
            fm = JobCreationForm(req.POST)
            if fm.is_valid():
                messages.success(req, "New job added successfully!")
                obj = fm.save()
                # job = Job.objects.get(pk=obj.id)
                # job.people.add(req.user)
                return HttpResponseRedirect('/dashboard/%i' % id)
        else:
            fm = JobCreationForm()
            return render(req, "add_job.html", {'group': id, 'form': fm})
    else:
        messages.warning(req, "You are not authorized to add a new job")
        return HttpResponseRedirect('/')


def edit_job(req, id, jobid):
    user_group = Group.objects.get(name = 'Terraformers')

    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        if req.method == 'POST':
            job = Job.objects.get(pk=jobid)
            fm = JobCreationForm(req.POST, instance=job)
            if fm.is_valid():
                messages.success(req, "Job updated successfully!")
                fm.save()
                return HttpResponseRedirect('/dashboard/%i' % id)
        else:
            job = Job.objects.get(pk=jobid)
            fm = JobCreationForm(instance=job)
            return render(req, "edit_job.html", {'group': id, 'form': fm})
    else:
        messages.warning(req, "You are not authorized to edit a job")
        return HttpResponseRedirect('/')


def archieve_job(req, id, jobid):
    user_group = Group.objects.get(name = 'Terraformers')
    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        job = Job.objects.get(pk=jobid)
        job.is_archieved = not job.is_archieved
        job.save()
        return HttpResponseRedirect('/dashboard/%i' % id)
    else:
        messages.warning(req, "You are not authorized to archieve a job")
        return HttpResponseRedirect('/')


def delete_job(req, id, jobid):
    user_group = Group.objects.get(name = 'Terraformers')
    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        job = Job.objects.get(pk=jobid)
        job.delete()
        return HttpResponseRedirect('/dashboard/%i' % id)
    else:
        messages.warning(req, "You are not authorized to delete a job")
        return HttpResponseRedirect('/')


def apply_job(req, id, jobid):
    user_group = Group.objects.get(name = 'Applicants')
    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        job = Job.objects.get(pk=jobid)
        if(job.people.filter(id=req.user.id)):
            job.people.remove(req.user)
            messages.success(req, "job Unappliced successfully")
        else:
            job.people.add(req.user)
            messages.success(req, "Job applied successfully!!")
        job.save()
        return HttpResponseRedirect('/dashboard/%i' % id)
    else:
        messages.warning(req, "You are not authorized to apply for a job")
        return HttpResponseRedirect('/')


def candidates(req, id, jobid):
    if id==1:
        user_group = Group.objects.get(name = 'Terraformers')
        category = 'Terraformer'
    else:
        user_group = Group.objects.get(name = 'Applicants')
        category = 'Applicant'
    user_group = Group.objects.get(name = 'Terraformers')
    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        cadets = Job.objects.get(pk=jobid).people.all()
        job = Job.objects.get(pk=jobid)
        return render(req, 'candidates.html', {'category': category, 'candidates': cadets, 'group': id, 'job': job})
    else:
        messages.warning(req, "You are not authorized to view candidates.")
        return HttpResponseRedirect('/')


def checkout_job(req, id, jobid):
    if id==1:
        user_group = Group.objects.get(name = 'Terraformers')
        category = 'Terraformer'
    else:
        user_group = Group.objects.get(name = 'Applicants')
        category = 'Applicant'
    user_group = Group.objects.get(name = 'Applicants')
    if req.user.is_authenticated and user_group == req.user.groups.all()[0]:
        job = Job.objects.get(pk=jobid)
        if job.people.filter(id=req.user.id):
            is_applied = True
        else:
            is_applied = False
        return render(req, 'checkout.html', {'category': category, 'group': id, 'job': job, 'is_applied': is_applied})
    else:
        messages.warning(req, "You are can view it in the candidates section.")
        return HttpResponseRedirect('/')