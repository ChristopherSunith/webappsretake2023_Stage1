from django.db import models

from register.models import CustomUser


# Create your models here.
class ProjectTopic(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        app_label = 'spmsapp'


class ProjectProposal(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='proposals')
    supervisor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_projects')
    topic = models.ForeignKey(ProjectTopic, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)


class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
