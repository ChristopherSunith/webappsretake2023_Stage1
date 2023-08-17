from django import forms
from django.shortcuts import render, redirect
from .models import CustomUser, UserRole


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']  # Update the fields


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Retrieve selected role
            selected_role = request.POST.get('role')

            try:
                role = UserRole.objects.get(role=selected_role)

                # Assign permissions to the user based on the role
                for permission in role.permissions.all():
                    user.user_permissions.add(permission)

                # Redirect to a success page
                return redirect('success_page')

            except UserRole.DoesNotExist:
                # Handle the case where the selected role doesn't exist
                pass

    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'registration_form.html', context)
