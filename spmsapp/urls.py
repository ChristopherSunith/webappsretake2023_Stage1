from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='spmsapp/home.html'), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('administrator/', views.administrator_dashboard, name='administrator_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('supervisor/', views.supervisor_dashboard, name='supervisor_dashboard'),
    # Other URL patterns can be added here
]
