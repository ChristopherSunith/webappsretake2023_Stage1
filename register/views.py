from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm
from django.contrib import messages

from django.contrib.auth.models import Group

from spmsapp.models import ProjectProposal
from .models import UserRole, CustomUser


# ...

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = CustomUser.objects.create_user(username=username, email=email, password=password)

            role = request.POST.get('role')
            if role == 'student':
                student_role, _ = UserRole.objects.get_or_create(role='Student')
                user.roles.add(student_role)
            elif role == 'supervisor':
                supervisor_role, _ = UserRole.objects.get_or_create(role='Supervisor')
                user.roles.add(supervisor_role)
            elif role == 'administrator':
                admin_role, _ = UserRole.objects.get_or_create(role='Administrator')
                user.roles.add(admin_role)

            messages.success(request, 'User successfully created!')
            return redirect('register_user')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/registration_form.html', {'form': form})


# ...
class RegistrationFormView(FormView):
    template_name = 'register/registration_form.html'
    form_class = UserRegistrationForm
    success_url = '/'  # Replace with the desired success URL

# Other view functions in your register/views.py file


def propose_project(request, project_id):
    project = ProjectProposal.objects.get(id=project_id)
    if request.method == 'POST':
        project.student.notifications.create(message="Your project proposal has been sent to the supervisor.")
        messages.success(request, 'Project proposal sent to supervisor.')
        return redirect('dashboard')  # Redirect to student's dashboard
    return render(request, 'register/propose_project.html', {'project': project})
