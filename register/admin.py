from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, UserRole


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('roles',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

GROUP_PERMISSIONS = {
    'Administrator': [
        # Add all the permissions here
        'admin|logentry|add_logentry', 'admin|logentry|change_logentry', 'admin|logentry|delete_logentry',
        'admin|logentry|view_logentry',
        'auth|group|add_group', 'auth|group|change_group', 'auth|group|delete_group', 'auth|group|view_group',
        'auth|permission|add_permission', 'auth|permission|change_permission', 'auth|permission|delete_permission',
        'auth|permission|view_permission',
        'auth|user|add_user', 'auth|user|change_user', 'auth|user|delete_user', 'auth|user|view_user',
        'contenttypes|contenttype|add_contenttype', 'contenttypes|contenttype|change_contenttype',
        'contenttypes|contenttype|delete_contenttype', 'contenttypes|contenttype|view_contenttype',
        'register|customuser|add_customuser', 'register|customuser|change_customuser',
        'register|customuser|delete_customuser', 'register|customuser|view_customuser',
        'register|notification|add_notification', 'register|notification|change_notification',
        'register|notification|delete_notification', 'register|notification|view_notification',
        'register|projectproposal|add_projectproposal', 'register|projectproposal|change_projectproposal',
        'register|projectproposal|delete_projectproposal', 'register|projectproposal|view_projectproposal',
        'register|projecttopic|add_projecttopic', 'register|projecttopic|change_projecttopic',
        'register|projecttopic|delete_projecttopic', 'register|projecttopic|view_projecttopic',
        'register|report|add_report', 'register|report|change_report', 'register|report|delete_report',
        'register|report|view_report',
        'register|userrole|add_userrole', 'register|userrole|change_userrole', 'register|userrole|delete_userrole',
        'register|userrole|view_userrole',
        'sessions|session|add_session', 'sessions|session|change_session', 'sessions|session|delete_session',
        'sessions|session|view_session',
    ],
}

# Create or update groups and assign permissions
for group_name, permissions in GROUP_PERMISSIONS.items():
    group, _ = Group.objects.get_or_create(name=group_name)
    permission_ids = []
    for permission_code in permissions:
        app_label, model, codename = permission_code.split('|')
        try:
            permission = Permission.objects.get(content_type__app_label=app_label, content_type__model=model,
                                                codename=codename)
            permission_ids.append(permission.id)
        except Permission.DoesNotExist:
            print(f"Permission not found: {permission_code}")
    group.permissions.set(permission_ids)


class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['role', 'display_permissions']

    def display_permissions(self, obj):
        return ', '.join(GROUP_PERMISSIONS.get(obj.role, []))

    display_permissions.short_description = 'Permissions'


admin.site.register(UserRole, UserRoleAdmin)

