from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from spmsapp.models import ProjectProposal, ProjectTopic
from register.models import CustomUser
from register.forms import UserRegistrationForm


def home(request):
    return render(request, 'home.html')


@require_POST
def home(request):
    print("Received request with method:", request.method)
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to appropriate dashboard
        else:
            # Handle authentication error
            error_message = 'Invalid credentials'
    else:
        error_message = None

    return render(request, 'spmsapp/home.html', {'form': form, 'error_message': error_message})


@login_required
def administrator_dashboard(request):
    if request.user.roles.filter(role='Administrator').exists():
        # Fetch data or perform actions specific to administrators
        users = CustomUser.objects.all()
        topics = ProjectTopic.objects.all()
        return render(request, 'spmsapp/dashboard/administrator_dashboard.html', {'users': users, 'topics': topics})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})


@login_required
def supervisor_dashboard(request):
    if request.user.roles.filter(role='Supervisor').exists():
        # Fetch data or perform actions specific to supervisors
        # For example, fetch project proposals assigned to this supervisor
        proposals = ProjectProposal.objects.filter(supervisor=request.user)
        return render(request, 'spmsapp/dashboard/supervisor_dashboard.html', {'proposals': proposals})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})


@login_required
def student_dashboard(request):
    if request.user.roles.filter(role='Student').exists():
        # Fetch data or perform actions specific to students
        # For example, fetch project proposals available for selection
        proposals = ProjectProposal.objects.filter(accepted=False)
        return render(request, 'spmsapp/dashboard/student_dashboard.html', {'proposals': proposals})
    else:
        return render(request, 'error.html', {'message': 'You are not authorized to access this page.'})
