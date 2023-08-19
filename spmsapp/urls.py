from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from spmsapp import views as spmsapp_views
from register import views
from spmsapp import views

app_name = 'spmsapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('home/', TemplateView.as_view(template_name='spmsapp/home.html'), name='home'),  # Change this to 'home' URL
    # ...
    # path('administrator/', views.administrator_dashboard, name='administrator_dashboard'),
    # Define URL for registration form view
    path('register/', include('register.urls')),
    # ...
    # remove the below path later
    # ... other URL patterns ...
    path('administrator/', views.administrator_dashboard, name='administrator_dashboard'),
    # ... other URL patterns ...
]
